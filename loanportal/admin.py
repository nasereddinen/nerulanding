from django.apps import apps
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *

app = apps.get_app_config('loanportal')


class LoanAdmin(ImportExportModelAdmin):
    list_display = ('user', 'company_name', 'interest_rate', 'term_length', 'created_at', 'updated_at')


admin.site.register(Loan, LoanAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'fieldname_download')


admin.site.register(Document, DocumentAdmin)
