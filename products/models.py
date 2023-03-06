from django.core.validators import MinValueValidator
from django.db import models

from dynamic.models import Subdomain
from services.StripeService import StripeService
from user.models import Profile

recurring_choices = (
    (1, "One time"),
    (2, "Monthly"),
    (3, "Yearly")
)

available_user_steps = {"Website Monthly": (50.00, 2),
                        "Toll Free Number Monthly": (40.00, 2),
                        "Fax Number Monthly": (40.00, 2),
                        "Domain Monthly": (13.99, 2),
                        "Professional Email Address Monthly": (7.99, 2),
                        "Website Yearly": (300, 3),
                        "Toll Free Number Yearly": (420, 3),
                        "Fax Number Yearly": (240, 3),
                        "Domain Yearly": (13.99, 3),
                        "Professional Email Address Yearly": (42, 3),
                        "Business builder program Monthly": (109.99, 2),
                        "Business builder program Yearly": (999, 3),
                        }

user_steps_choices = [(i, i) for i in available_user_steps.keys()]


class Tradelines(models.Model):
    company_name = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    tradeline_amount = models.DecimalField(max_digits=100, decimal_places=2)
    tradeline_credit_amount = models.CharField(max_length=500, null=True, blank=True)
    company_reports_to = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, default=0, decimal_places=2, validators=[MinValueValidator(0)])
    charge = models.DecimalField(max_digits=100, default=0, decimal_places=2, validators=[MinValueValidator(0)])
    video_link = models.URLField(max_length=300, null=True, blank=True)
    tier = models.CharField(max_length=10, null=True, blank=True)
    whitelabel_portal = models.ForeignKey(Subdomain, on_delete=models.CASCADE, null=True, blank=True)

    product_id = models.CharField(max_length=100, null=True)
    price_id = models.CharField(max_length=100, null=True)
    price_lookup = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "1. Tradeline"
        verbose_name_plural = "1. Tradelines"

    def __str__(self):
        return f"{self.company_name} {self.product} tradeline"

    def save(self, *args, **kwargs):
        if self.price < 0 or self.charge < 0:
            return

        if not self.product_id:
            response = StripeService.create_product(str(self), float(self.price) + float(self.charge), self.company_name)
            self.product_id = response['prod_id']
            self.price_id = response['price_id']
            self.price_lookup = response['price_lookup']
        else:
            price_id, _ = StripeService.update_product(self.product_id, self.price_id, str(self),
                                                       float(self.price) + float(self.charge))
            if price_id != self.price_id:
                self.price_id = price_id
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        StripeService.delete_product(self.product_id)
        super().delete(*args, **kwargs)


class UserStepsProduct(models.Model):

    name = models.CharField(max_length=200, choices=user_steps_choices)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    recurring = models.IntegerField(choices=recurring_choices, null=True)

    whitelabel_portal = models.ForeignKey(Subdomain, on_delete=models.CASCADE, null=True, blank=True)

    product_id = models.CharField(max_length=100, null=True)
    price_id = models.CharField(max_length=100, null=True)
    price_lookup = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "2. User Steps"
        verbose_name_plural = "2. User Steps"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if self.name in available_user_steps:
            if self.price < available_user_steps[self.name][0]:
                return

        if not self.product_id:
            response = StripeService.create_product(self.name, self.price, recurring=self.recurring)
            self.product_id = response['prod_id']
            self.price_id = response['price_id']
            self.price_lookup = response['price_lookup']
        else:
            price_id, lookup_key = StripeService.update_product(
                self.product_id,
                self.price_id,
                self.name,
                self.price,
                recurring=self.recurring)

            if price_id != self.price_id:
                self.price_id = price_id
            if lookup_key != self.price_lookup:
                self.price_lookup = lookup_key

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        StripeService.delete_product(self.product_id)
        super().delete(*args, **kwargs)
