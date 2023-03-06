from django.db import models
from django.utils import timezone
from user.models import Profile

app_name = 'yourplan'


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class YourPlan(ModelMixin, models.Model):
    class Meta:
        db_table = 'yourplan'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    name = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    report_to = models.CharField(max_length=500, null=True)
    monthly_payment = models.CharField(max_length=15, null=True)
    estimated_term = models.CharField(max_length=500, null=True)
    estimated_amount = models.CharField(max_length=5, null=True)
    payment_terms = models.CharField(max_length=500, null=True)
    terms = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Klarna(ModelMixin, models.Model):
    class Meta:
        db_table = 'klarna'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class Paypal(ModelMixin, models.Model):
    class Meta:
        db_table = 'paypal'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class Quadpay(ModelMixin, models.Model):
    class Meta:
        db_table = 'quadpay'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class Sezzle(ModelMixin, models.Model):
    class Meta:
        db_table = 'sezzle'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class Affirm(ModelMixin, models.Model):
    class Meta:
        db_table = 'affirm'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class Behalf(ModelMixin, models.Model):
    class Meta:
        db_table = 'behalf'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class FundBoxPay(ModelMixin, models.Model):
    class Meta:
        db_table = 'fundboxpay'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class InvoiceFactoringPayment(ModelMixin, models.Model):
    class Meta:
        db_table = 'invoicefactoringpayment'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class Viabill(ModelMixin, models.Model):
    class Meta:
        db_table = 'viabill'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class RegularPayment(ModelMixin, models.Model):
    class Meta:
        db_table = 'regularpayment'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()


class Stripe(ModelMixin, models.Model):
    class Meta:
        db_table = 'stripe'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    how_much_owed = models.CharField(max_length=500)
    financed_so_far = models.CharField(max_length=500)
    payment_left = models.CharField(max_length=500)
    payment_terms = models.CharField(max_length=500)

    def __str__(self):
        return self.user.user.get_full_name()
