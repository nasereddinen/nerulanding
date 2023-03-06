from django.contrib import admin

# Register your models here.
from financing_portal.models import Product, ProductPurchasedModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'recurring')
    readonly_fields = ('product_id', 'price_id', 'price_lookup')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPurchasedModel, admin.ModelAdmin)
