from django.contrib import admin

# Register your models here.
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['finalize_url', 'timestamp', 'updated']

admin.site.register(Order, OrderAdmin)