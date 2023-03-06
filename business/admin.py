from django.apps import apps
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *

app = apps.get_app_config('business')



class BusinessCreditStepsAdmin(admin.ModelAdmin):
    list_display = ("user", )
    list_filter = ('user',)


admin.site.register(BusinessCreditSteps, BusinessCreditStepsAdmin)


class FinancingInformationAdmin(admin.ModelAdmin):
    list_display = ("user", 'created_at', 'updated_at')
    list_filter = ('user',)


admin.site.register(FinancingInformation, FinancingInformationAdmin)


class CreditRepairInformationAdmin(admin.ModelAdmin):
    list_display = ("user", 'created_at', 'updated_at')
    list_filter = ('user',)


admin.site.register(CreditRepairInformation, CreditRepairInformationAdmin)


class BusinessCreditInformationAdmin(admin.ModelAdmin):
    list_display = ("user", 'created_at', 'updated_at')
    list_filter = ('user',)


admin.site.register(BusinessCreditInformation, BusinessCreditInformationAdmin)


class DomainResource(resources.ModelResource):
    class Meta:
        model = Domain
        exclude = ('created_at', 'updated_at')


class DomainAdmin(ImportExportModelAdmin):
    resource_class = DomainResource


admin.site.register(Domain, DomainAdmin)


class NoCreditCheckLoanResource(resources.ModelResource):
    class Meta:
        model = NoCreditCheckLoans
        exclude = ('created_at', 'updated_at')


class NoCreditCheckLoanAdmin(ImportExportModelAdmin):
    resource_class = NoCreditCheckLoanResource
    list_display = ('lender_name', 'created_at', 'updated_at')


admin.site.register(NoCreditCheckLoans, NoCreditCheckLoanAdmin)


# class RevolvingCreditResource(resources.ModelResource):
#     class Meta:
#         model = RevolvingCredit
#         exclude = ('created_at', 'updated_at')
#
#
# class RevolvingCreditAdmin(ImportExportModelAdmin):
#     resource_class = RevolvingCreditResource
#
# admin.site.register(RevolvingCredit, RevolvingCreditAdmin)


# class LenderResource(resources.ModelResource):
#     class Meta:
#         model = Lender
#         exclude = ('created_at', 'updated_at')
#
#
# class LenderAdmin(ImportExportModelAdmin):
#     resource_class = LenderResource
#
#
# admin.site.register(Lender, LenderAdmin)


class ShortTermLoanResource(resources.ModelResource):
    class Meta:
        model = ShortTermLoan
        exclude = ('created_at', 'updated_at')


class ShortTermLoanAdmin(ImportExportModelAdmin):
    resource_class = ShortTermLoanResource


admin.site.register(ShortTermLoan, ShortTermLoanAdmin)


class InvoiceFactoringResource(resources.ModelResource):
    class Meta:
        model = InvoiceFactoring
        exclude = ('created_at', 'updated_at')


class InvoiceFactoringAdmin(ImportExportModelAdmin):
    resource_class = InvoiceFactoringResource


admin.site.register(InvoiceFactoring, InvoiceFactoringAdmin)


class InvoiceFinancingResource(resources.ModelResource):
    class Meta:
        model = InvoiceFinancing
        exclude = ('created_at', 'updated_at')


class InvoiceFinancingAdmin(ImportExportModelAdmin):
    resource_class = InvoiceFinancingResource


admin.site.register(InvoiceFinancing, InvoiceFinancingAdmin)


class EquipmentFinancingResource(resources.ModelResource):
    class Meta:
        model = EquipmentFinancing
        exclude = ('created_at', 'updated_at')


class EquipmentFinancingAdmin(ImportExportModelAdmin):
    resource_class = EquipmentFinancingResource


admin.site.register(EquipmentFinancing, EquipmentFinancingAdmin)


class LinesOfCreditResource(resources.ModelResource):
    class Meta:
        model = LinesOfCredit
        exclude = ('created_at', 'updated_at')


class LinesOfCreditAdmin(ImportExportModelAdmin):
    resource_class = LinesOfCreditResource


admin.site.register(LinesOfCredit, LinesOfCreditAdmin)


class SbaLoanResource(resources.ModelResource):
    class Meta:
        model = SbaLoan
        exclude = ('created_at', 'updated_at')


class SbaLoanAdmin(ImportExportModelAdmin):
    resource_class = SbaLoanResource


admin.site.register(SbaLoan, SbaLoanAdmin)


class BusinessTermLoanResource(resources.ModelResource):
    class Meta:
        model = BusinessTermLoan
        exclude = ('created_at', 'updated_at')


class BusinessTermLoanAdmin(ImportExportModelAdmin):
    resource_class = BusinessTermLoanResource


admin.site.register(BusinessTermLoan, BusinessTermLoanAdmin)


class StoreCreditVendorListResource(resources.ModelResource):
    class Meta:
        model = StoreCreditVendorList
        exclude = ('created_at', 'updated_at')


class StoreCreditVendorListAdmin(ImportExportModelAdmin):
    resource_class = StoreCreditVendorListResource


admin.site.register(StoreCreditVendorList, StoreCreditVendorListAdmin)


class StarterVendorListResource(resources.ModelResource):
    class Meta:
        model = StarterVendorList
        exclude = ('created_at', 'updated_at')


class StarterVendorListAdmin(ImportExportModelAdmin):
    resource_class = StarterVendorListResource


admin.site.register(StarterVendorList, StarterVendorListAdmin)


class PersonalCreditCardResource(resources.ModelResource):
    class Meta:
        model = PersonalCreditCard
        exclude = ('created_at', 'updated_at')


class PersonalCreditCardAdmin(ImportExportModelAdmin):
    resource_class = PersonalCreditCardResource


admin.site.register(PersonalCreditCard, PersonalCreditCardAdmin)


class BusinessCreditCardResource(resources.ModelResource):
    class Meta:
        model = BusinessCreditCard
        exclude = ('created_at', 'updated_at')


class BusinessCreditCardAdmin(ImportExportModelAdmin):
    resource_class = BusinessCreditCardResource


admin.site.register(BusinessCreditCard, BusinessCreditCardAdmin)


class PersonalLoanResource(resources.ModelResource):
    class Meta:
        model = PersonalLoan
        exclude = ('created_at', 'updated_at')


class PersonalLoanAdmin(ImportExportModelAdmin):
    resource_class = PersonalLoanResource


admin.site.register(PersonalLoan, PersonalLoanAdmin)


class RevolvingBusinessCreditVendorResource(resources.ModelResource):
    class Meta:
        model = RevolvingBusinessCreditVendor
        exclude = ('created_at', 'updated_at')


class RevolvingBusinessCreditVendorAdmin(ImportExportModelAdmin):
    resource_class = RevolvingBusinessCreditVendorResource


admin.site.register(RevolvingBusinessCreditVendor, RevolvingBusinessCreditVendorAdmin)


class NopgResource(resources.ModelResource):
    class Meta:
        model = Nopg
        exclude = ('created_at', 'updated_at')


class NopgAdmin(ImportExportModelAdmin):
    resource_class = NopgResource


admin.site.register(Nopg, NopgAdmin)


class PersonalCreditTradeLineResource(resources.ModelResource):
    class Meta:
        model = PersonalCreditTradeLine
        exclude = ('created_at', 'updated_at')


class PersonalCreditTradeLineAdmin(ImportExportModelAdmin):
    resource_class = PersonalCreditTradeLineResource


admin.site.register(PersonalCreditTradeLine, PersonalCreditTradeLineAdmin)

for model in app.get_models():
    try:
        admin.site.register(model)
    except:
        pass
