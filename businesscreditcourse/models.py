from django.db import models
from django.utils import timezone
from user.models import Profile


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class BusinessCreditCourse(ModelMixin, models.Model):
    class Meta:
        db_table = 'businesscreditcourse'

    name = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    report_to = models.CharField(max_length=500, null=True)
    monthly_payment = models.CharField(max_length=500, null=True)
    estimated_term = models.CharField(max_length=500, null=True)
    estimated_amount = models.CharField(max_length=500, null=True)
    payment_terms = models.CharField(max_length=500, null=True)
    terms = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
