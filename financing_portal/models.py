from django.conf import settings
from django.db import models
from core.models import ProductModel


class Product(ProductModel):
    description = models.TextField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)


class ProductPurchasedModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payments_left = models.DecimalField(max_digits=100, default=0, decimal_places=2)
    amount_left = models.DecimalField(max_digits=100, default=0, decimal_places=2)
    username = models.CharField(blank=True, null=True, max_length=50)
    password = models.CharField(blank=True, null=True, max_length=50)
    link = models.URLField(blank=True, null=True)
    logged_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} {self.user}"
