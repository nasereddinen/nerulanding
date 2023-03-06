import os
import uuid

from django.db import models
from django.utils.safestring import mark_safe
from user.models import Profile

app_name = 'loansportal'


def get_file_path(instance, filename):
    return os.path.join(f'documents/loans/{uuid.uuid4()}', filename)


class Loan(models.Model):
    class Meta:
        db_table = 'Loan'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    company_name = models.CharField(max_length=50, null=True)
    interest_rate = models.CharField(max_length=500, null=True)
    term_length = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.user.get_full_name() + " " + self.company_name


class Document(models.Model):
    class Meta:
        db_table = 'Document'
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name=f'{app_name}%(class)s_profile')
    type = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to=get_file_path, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.user.get_full_name() + " " + self.type

    def fieldname_download(self):
        return mark_safe(f'<a href="{self.document.url}">Download</a>')
