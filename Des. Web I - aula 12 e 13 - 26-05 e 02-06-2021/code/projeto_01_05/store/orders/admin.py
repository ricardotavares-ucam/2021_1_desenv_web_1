from django.contrib import admin
from .models import OrderItem, Order

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    fields = ('product', 'quantity', 'get_cost')
    readonly_fields = ('get_cost',)

class OrderAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'address', 'postal_code', 'get_total_price')
    list_display = ['__str__', 'user', 'name', 'address', 'get_total_price']
    inlines = [OrderItemInline]
    readonly_fields = ('get_total_price',)
admin.site.register(Order, OrderAdmin)

