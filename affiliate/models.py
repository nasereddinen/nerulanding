from django.db import models
from django.utils import timezone
from user.models import Profile

app_name = 'affiliate'


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Residual(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_residual'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    amountofresiduals = models.CharField(max_length=500, null=True)
    product = models.CharField(max_length=500, null=True)
    payout_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class ShareLinks(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_sharelink'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    facebook_link = models.CharField(max_length=500, null=True)
    text_link = models.CharField(max_length=500, null=True)
    email_link = models.CharField(max_length=500, null=True)
    twitter = models.CharField(max_length=500, null=True)
    instagram = models.CharField(max_length=500, null=True)
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


class Lead(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_lead'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    business_name = models.CharField(max_length=100, null=True)
    business_package = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class AffiliateAgents(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_affiliate_agents'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    full_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
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


class PaypalInformation(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_paypal_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    paypal_email = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()


class Webinar(ModelMixin, models.Model):
    class Meta:
        db_table = f'{app_name}_webinars'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    link = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.get_full_name()
