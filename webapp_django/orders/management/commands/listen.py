from django.core.management.base import BaseCommand
from orders.models import Order
import json
import mykafka 


class Command(BaseCommand):
    help = 'Process orders'

    def handle(self, *args, **options):
        # Your logic to process orders goes here
        consumer = mykafka.get_consumer(topics=['order_update'])

        for message in consumer:
            try:
                self.process_message(message)
            except Exception as e:
                print(f'Error processing message: {e}')
    
    def process_message(self, message):
        raw_value = message.value
        value_str = raw_value.decode("utf-8")
        try:
            data = json.loads(value_str)
        except json.decoder.JSONDecodeError:
            data = None
            print("invalid json")
        # print(data, type(data), type(value_str))
        data_type = data.get('type')
        order_shipped_type = f"orders/{Order.OrderStatus.SHIPPED}"
        if data_type == order_shipped_type:
            print(data)
            # order_id = data.get('order_id')
            # qs = Order.objects.filter(id__iexact=order_id).exclude(status=Order.OrderStatus.SHIPPED)
            # if qs.exists():
            #     qs.update(status=Order.OrderStatus.SHIPPED)
