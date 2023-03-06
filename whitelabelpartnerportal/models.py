import os
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from core.models import ProductModel
from services.FileServices import get_file_path
from user.models import Profile
from phonenumber_field.modelfields import PhoneNumberField

app_name = 'whitelabelpartnerportal'


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Residual(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_residual'

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    business_name = models.CharField(max_length=200, null=True)
    commissions_made = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    amountofresiduals = models.CharField(max_length=500, null=True)
    product = models.CharField(max_length=500, null=True)
    payout_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class BecomingAPartner(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_becomingapartner'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    business_name = models.CharField(max_length=500, null=True)
    business_number = models.CharField(max_length=500, null=True)
    logo = models.FileField(upload_to=get_file_path, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Lead(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_lead'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    first_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500, null=True)
    business_name = models.CharField(max_length=500, null=True)
    business_package = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class AffiliateAgents(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_affiliate_agents'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    full_name = models.CharField(max_length=500, null=True)
    phone_number = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Sale(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_sale'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    sales = models.CharField(max_length=500, null=True)
    product = models.CharField(max_length=500, null=True)
    payout_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class AffiliateResidual(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_affiliate_residual'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    amount = models.CharField(max_length=500, null=True)
    affiliate_name = models.CharField(max_length=500, null=True)
    payout_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Credit(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_credit'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    account_name = models.CharField(max_length=500, null=True)
    created = models.CharField(max_length=500, null=True, default='')
    applied = models.CharField(max_length=500, null=True, default='')
    amount = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class FreeProgram(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_free_program'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    client_name = models.CharField(max_length=500, null=True)
    client_email = models.CharField(max_length=500, null=True)
    client_phone_number = models.CharField(max_length=500, null=True)
    updates_made = models.CharField(max_length=500, null=True)
    residual_amount = models.CharField(max_length=500, null=True)
    expected_payout = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class SignedUpProgram(ModelMixin,models.Model):
    class Meta:
        db_table = f'{app_name}_signedup_program'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    client_name = models.CharField(max_length=500, null=True)
    client_email = models.CharField(max_length=500, null=True)
    client_phone_number = models.CharField(max_length=500, null=True)
    updates_made = models.CharField(max_length=500, null=True,default="N/A")
    residual_amount = models.CharField(max_length=500, null=True,default="N/A")
    expected_payout = models.CharField(max_length=500, null=True,default="N/A")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()



class PaidProgram(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_paid_program'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    client_name = models.CharField(max_length=500, null=True)
    client_email = models.CharField(max_length=500, null=True)
    client_phone_number = models.CharField(max_length=500, null=True)
    updates_made = models.CharField(max_length=500, null=True)
    residual_amount = models.CharField(max_length=500, null=True)
    expected_payout = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Invoice(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_invoice'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    product = models.CharField(max_length=500, null=True)
    invoiceamount = models.CharField(max_length=500, null=True)
    invoiceduedate = models.DateTimeField(null=True)
    status = models.CharField(max_length=500, null=True)
    paynow = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Order(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_order'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    order_placed = models.CharField(max_length=500, null=True)
    date_ordered = models.DateTimeField(null=True)
    order_amount = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Payment(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_payments'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    payment = models.CharField(max_length=500, null=True)
    account_name = models.CharField(max_length=500, null=True)
    amount_paid = models.CharField(max_length=500, null=True)
    date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class BankPaymentInformation(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_bank_payment_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    routing_number = models.CharField(max_length=500, null=True)
    name_of_bank = models.CharField(max_length=500, null=True)
    account_number = models.CharField(max_length=500, null=True)
    name_on_bank_account = models.CharField(max_length=500, null=True)
    your_address = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class ZelleInformation(models.Model, ModelMixin):
    user= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    zelle_email=models.EmailField(max_length=500, null=True,blank=True)
    zelle_phone=PhoneNumberField(max_length=500, null=True,blank=True)

    def __str__(self):
        return self.user.user.get_full_name()

    class Meta:
        db_table = f'{app_name}_zelle_information'


class PaypalInformation(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_paypal_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    paypal_email = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class WhitelabelWebsite(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_whitelabel_website'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    website_name = models.CharField(max_length=500, null=True)
    website_link = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class MarketingRoi(ModelMixin, models.Model):
    current_date = models.DateField(null=True, blank=True)
    amount_spent = models.CharField(max_length=100, null=True, blank=True)
    amount_left = models.CharField(max_length=100, null=True, blank=True)
    amount_made = models.CharField(max_length=100, null=True, blank=True)
    payout_date = models.DateField(null=True, blank=True)

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.get_full_name()


class WhitelabelPortal(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_whitelabel_portal'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    portal_link = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class WhitelabelBusinessPackage(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_whitelabel_business_package'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    website_login = models.CharField(max_length=500, null=True)
    toll_free_number_login = models.CharField(max_length=500, null=True)
    professional_email_address_login = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class WholeSale(ProductModel):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)


class WholeSaleOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(WholeSale, on_delete=models.CASCADE, null=True)


class ClientsOnWholeSale(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    client_name = models.CharField(max_length=100, null=True)
    package = models.ForeignKey(WholeSale, null=True, on_delete=models.CASCADE)


class Resource(models.Model):
    name = models.CharField(max_length=100, null=True)
    # url = models.URLField(null=True)
    document = models.FileField(upload_to=get_file_path, null=True)
    category = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
