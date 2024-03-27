import uuid

from django.db import models
from django.db.models.signals import post_save

from django.utils.safestring import mark_safe
import mykafka

from . import utils as orders_utils


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PROCESSED = 'processed', 'Processed'
        SHIPPED = 'shipped', 'Shipped'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    is_shipped = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        if not self.product_name:
            self.product_name = orders_utils.generate_product_name()
        if self.is_shipped:
            self.status = Order.OrderStatus.SHIPPED
        super().save(*args, **kwargs)

    def ready_to_ship(self):
        return self.status == self.OrderStatus.PROCESSED

    def shipped(self):
        return self.status == self.OrderStatus.SHIPPED
    
    def serialize(self):
        return {
            "id": str(self.id),
            "product_name": self.product_name,
            "status": self.status,
            "timestamp": self.timestamp.timestamp()
        }
    
    def finalize_url(self):
        fastapi_url = f"http://localhost:8000/order/{self.id}"
        return mark_safe(f"<a href='{fastapi_url}' target='_blank'>{fastapi_url}</a>")

    
    

def order_did_update(sender, instance, *args, **kwargs):
    if instance.ready_to_ship() and not instance.is_shipped: 
        instance_data = instance.serialize()
        topic_status = Order.OrderStatus.PROCESSED
        topic_data = {
            "type": f"orders/{topic_status}",
            "object": instance_data,
        }
        # print(topic_data)
        result = mykafka.send_topic_data(topic_data, topic=f'order_update')
        # print(result)


post_save.connect(order_did_update, sender=Order)