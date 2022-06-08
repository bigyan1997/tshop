from django.contrib import admin
from .models import Payment, Order, OrderProduct


# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered',
                    'created_at']
    list_filter = ['status', 'is_ordered']
    list_editable = ['status',]
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_method', 'payment_id', 'amount_paid', 'status', 'created_at']
    list_filter = ['user', 'payment_method']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
