from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from core.models import BusinessTierModel, TimeTrackedModel
from user.models import Profile

from django.db.models.signals import pre_save
from django.dispatch import receiver
from urllib.parse import urlparse


class ModelMixin:
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    @property
    def get_url(self):
        if hasattr(self, 'url'):
            if not self.url.startswith("http"):
                return "http://" + self.url
            else:
                return self.url


class BusinessCreditSteps(TimeTrackedModel):
    class Meta:
        verbose_name = "Business Credit steps"
        verbose_name_plural = "Business Credit steps"

    choices = (
        ("1", "Dentist"),
        ("2", "Real Estate"),
        ("3", "Restaurant"),
        ("4", "Auto Repair"),
        ("5", "Trucking"),
        ("6", "Hair Salon"),
        ("7", "Transportation Services"),
        ("8", "Electrician"),
        ("9", "Lawyer"),
        ("10", "Photography"),
        ("11", "Landscaping"),
        ("12", "Musician"),
        ("13", "Ecommece"),
        ("14", "Insurance Agent"),
        ("15", "Accountant"),
        ("16", "Carpet & Flooring"),
        ("17", "Barber"),
        ("18", "Spa"),
        ("19", "Wedding Planner"),
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=5000, null=True,)
    last_name = models.CharField(max_length=5000, null=True)
    email = models.CharField(max_length=5000, null=True)
    phone = models.CharField(max_length=5000, null=True)
    website = models.BooleanField(default=False)
    fax = models.BooleanField(default=False)
    toll_free_number = models.BooleanField(default=False)
    domain = models.BooleanField(default=False)
    pro_email_address = models.BooleanField(default=False)
    website_inndustry = models.CharField(max_length=5000, null=True, blank=True, choices=choices)


class FinancingInformation(TimeTrackedModel):
    class Meta:
        db_table = 'financing_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    experian = models.CharField(max_length=5000)
    equifax = models.CharField(max_length=5000)
    transunion = models.CharField(max_length=5000)
    monthly_revenue_3 = models.CharField(max_length=5000)
    daily_balance_3 = models.CharField(max_length=5000)
    monthlty_ending_balance_3 = models.CharField(max_length=5000)
    monthly_revenue_6 = models.CharField(max_length=5000)
    daily_balance_6 = models.CharField(max_length=5000)
    monthlty_ending_balance_6 = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    nonsufficient_6 = models.CharField(max_length=5000)
    nonsufficient_12 = models.CharField(max_length=5000)
    current_liens = models.CharField(max_length=5000)
    business_account = models.CharField(max_length=5000)
    business_loan = models.CharField(max_length=5000)
    business_age = models.CharField(max_length=5000)


class CreditRepairInformation(TimeTrackedModel):
    class Meta:
        db_table = 'credit_repair_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    experian_score = models.CharField(max_length=5000)
    equifax_score = models.CharField(max_length=5000)
    transunion_score = models.CharField(max_length=5000)
    experian_utilization = models.CharField(max_length=5000)
    equifax_utilization = models.CharField(max_length=5000)
    transunion_utilization = models.CharField(max_length=5000)
    current_collections = models.CharField(max_length=5000)
    bankruptcies = models.CharField(max_length=5000)
    bankruptcies_10 = models.CharField(max_length=5000)
    inquiries = models.CharField(max_length=5000)
    missed_payments = models.CharField(max_length=5000)
    current_acc_experian = models.CharField(max_length=5000)
    current_acc_equifax = models.CharField(max_length=5000)
    current_acc_transunion = models.CharField(max_length=5000)
    credit_history_experian = models.CharField(max_length=5000)
    credit_history_equifax = models.CharField(max_length=5000)
    credit_history_transunion = models.CharField(max_length=5000)


class BusinessCreditInformation(TimeTrackedModel):
    class Meta:
        db_table = 'businesscredit_information'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_time = models.CharField(max_length=5000, null=True)
    trade_lines = models.CharField(max_length=5000, null=True)


class Domain(TimeTrackedModel):
    class Meta:
        db_table = 'domain'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=5000)
    domain_needed = models.CharField(max_length=5000)


class FinancingPlanRegularPerson(TimeTrackedModel):
    class Meta:
        db_table = 'financingplanregularperson'

    name = models.CharField(max_length=5000, null=True)
    description = models.CharField(max_length=5500, null=True)
    report_to = models.CharField(max_length=5000, null=True)
    monthly_payment = models.CharField(max_length=5000, null=True)
    estimated_term = models.CharField(max_length=5000, null=True)
    estimated_amount = models.CharField(max_length=5000, null=True)
    payment_terms = models.CharField(max_length=5000, null=True)
    terms = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.name


class EquipmentFinancing(TimeTrackedModel):
    class Meta:
        db_table = 'equipment_financing'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)

    def __str__(self):
        return self.lender_name


class Fax(TimeTrackedModel):
    class Meta:
        db_table = 'fax'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fax_needed = models.CharField(max_length=5000)


class InvoiceFactoring(TimeTrackedModel):
    class Meta:
        db_table = 'invoice_factoring'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)


class InvoiceFinancing(TimeTrackedModel):
    class Meta:
        db_table = 'invoice_financing'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)

    def __str__(self):
        return self.lender_name


class Category(models.Model):
    class Meta:
        db_table = 'category'

    title = models.CharField(max_length=5000)


class Lender(TimeTrackedModel):
    class Meta:
        db_table = 'lender'

    name = models.CharField(max_length=5000, null=True)
    description = models.CharField(max_length=5000, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    report_to = models.CharField(max_length=5000, null=True)
    monthly_payment = models.CharField(max_length=5000, null=True)
    estimated_term = models.CharField(max_length=5000, null=True)
    estimated_amount = models.CharField(max_length=5000, null=True)
    payment_terms = models.CharField(max_length=5000, null=True)
    terms = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.name


class LinesOfCredit(TimeTrackedModel):
    class Meta:
        db_table = 'lines_of_credit'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)

    def __str__(self):
        return self.lender_name


class Nopg(TimeTrackedModel):
    class Meta:
        db_table = 'nopg'

    name = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    reports_to = models.CharField(max_length=5000)
    estimated_amount = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class ProfessionalEmailAddress(TimeTrackedModel):
    class Meta:
        db_table = 'professional_email_address'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email_address_needed = models.CharField(max_length=5000)
    domain_present = models.CharField(max_length=5000)


class Progress(TimeTrackedModel):
    class Meta:
        db_table = 'progress'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    website_creation = models.CharField(max_length=5000)
    dns_number = models.CharField(max_length=5000)
    virtual_number = models.CharField(max_length=5000)
    fax_number = models.CharField(max_length=5000)
    toll_free_number = models.CharField(max_length=5000)
    business_bank_account = models.CharField(max_length=5000)
    listing = models.CharField(max_length=5000)
    professional_email_address = models.CharField(max_length=5000)
    domain = models.CharField(max_length=5000)


class Industry(models.Model):
    class Meta:
        db_table = 'industry'

    title = models.CharField(max_length=5000)


class RevenueLending(TimeTrackedModel):
    class Meta:
        db_table = 'revenue_lending'

    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fico_score = models.CharField(max_length=5000)
    equifax_score = models.CharField(max_length=5000)
    transunion_score = models.CharField(max_length=5000)
    avg_monthly_revenue = models.CharField(max_length=5000)
    abg_daily_balance = models.CharField(max_length=5000)
    avg_monthly_ending_balance = models.CharField(max_length=5000)
    business_debt = models.CharField(max_length=5000)
    liens = models.CharField(max_length=5000)
    business_bank_account = models.CharField(max_length=5000)
    age = models.IntegerField()
    registered_at = models.DateTimeField(null=True, blank=True)
    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)


class RevolvingCredit(TimeTrackedModel):
    class Meta:
        db_table = 'revolving_credit'

    name = models.CharField(max_length=5000)
    report_to = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class SbaLoan(TimeTrackedModel):
    class Meta:
        db_table = 'sba_loan'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)

    def __str__(self):
        return self.lender_name


class ShortTermLoan(TimeTrackedModel):
    class Meta:
        db_table = 'short_term_loan'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)

    def __str__(self):
        return self.lender_name


class BusinessTermLoan(TimeTrackedModel):
    class Meta:
        db_table = 'term_loan'

    lender_name = models.CharField(max_length=5000)
    personal_credit_score = models.CharField(max_length=5000)
    time_in_business = models.CharField(max_length=5000)
    business_revenue = models.CharField(max_length=5000)
    term_length = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    strategy = models.CharField(max_length=5000)

    def __str__(self):
        return self.lender_name


class StoreCreditVendorList(TimeTrackedModel):
    class Meta:
        db_table = 'store_credit_vendor_2'

    name = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    reports_to = models.CharField(max_length=5000)
    estimated_amount = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class StarterVendorList(TimeTrackedModel):
    class Meta:
        db_table = 'starter_vendor_list'

    name = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    report_to = models.CharField(max_length=5000)
    monthly_payment = models.CharField(max_length=5000)
    estimated_terms = models.CharField(max_length=5000)
    estimated_amount = models.CharField(max_length=5000)
    payment_terms = models.CharField(max_length=5000)


class TollFreeNumber(TimeTrackedModel):
    class Meta:
        db_table = 'toll_free_number'

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    toll_free_number_needed = models.CharField(max_length=5000)


class WebsiteCreation(TimeTrackedModel):
    class Meta:
        db_table = 'website_creation'

    industry_name = models.CharField(max_length=5000)
    booking_on_page = models.CharField(max_length=5000)
    business_name = models.CharField(max_length=5000)
    chat_bot = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    theme = models.CharField(max_length=5000)
    pages_needed = models.CharField(max_length=5000)
    services = models.CharField(max_length=5000)
    domain = models.CharField(max_length=5000)
    about_you = models.CharField(max_length=5500)
    url = models.CharField(max_length=5000)
    domain_owned = models.CharField(max_length=5000)


class PersonalCreditCard(TimeTrackedModel):
    class Meta:
        db_table = 'personal_credit_card'

    cc_name = models.CharField(max_length=5000)
    min_credit_score = models.CharField(max_length=5000)
    credit_bureau = models.CharField(max_length=5000)
    debt_ratio = models.CharField(max_length=5000)
    bankruptcy = models.CharField(max_length=5000)
    credit_data = models.CharField(max_length=5000)
    apr = models.CharField(max_length=5000)
    misc_info = models.CharField(max_length=5000)
    url = models.CharField(blank=True, max_length=5000)

    def __str__(self):
        return self.cc_name


class BusinessCreditCard(TimeTrackedModel):
    class Meta:
        db_table = 'business_credit_card'

    cc_name = models.CharField(null=True, max_length=5000)
    min_credit_score = models.CharField(null=True, max_length=5000)
    credit_bureau = models.CharField(null=True, max_length=5000)
    debt_ratio = models.CharField(null=True, max_length=5000)
    bankruptcy = models.CharField(null=True, max_length=5000)
    credit_data = models.CharField(null=True, max_length=5000)
    apr = models.CharField(null=True, max_length=5000)
    strategy = models.CharField(null=True, max_length=5000)
    max_inquiries = models.CharField(null=True, max_length=5000)
    url = models.CharField(blank=True, max_length=5000)

    def __str__(self):
        return self.cc_name


class PersonalLoan(TimeTrackedModel):
    class Meta:
        db_table = 'personal_loan'

    lender_name = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    inquiries = models.CharField(max_length=5000)
    credit_bureau = models.CharField(max_length=5000)
    states = models.CharField(max_length=5000)
    credit_score = models.CharField(max_length=5000)
    emp_length = models.CharField(max_length=5000)
    credit_history = models.CharField(max_length=5000)
    url = models.CharField(blank=True, max_length=5000)

    def __str__(self):
        return self.lender_name


class RevolvingBusinessCreditVendor(TimeTrackedModel):
    class Meta:
        db_table = 'revolving_business_credit'

    name = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    terms = models.CharField(max_length=5000)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    report_to = models.CharField(max_length=5000)
    url = models.CharField(blank=True, max_length=5000)

    def __str__(self):
        return self.name


class NoCreditCheckLoans(TimeTrackedModel):
    class Meta:
        db_table = 'nocreditcheck_loans'

    lender_name = models.CharField(null=True, max_length=5000)
    estimated_terms = models.CharField(null=True, max_length=5000)
    url = models.CharField(null=True, max_length=5000)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.lender_name


class PersonalCreditTradeLine(TimeTrackedModel):
    class Meta:
        db_table = 'personal_credit_tradeline'

    lender_name = models.CharField(max_length=500)
    hard_check = models.CharField(max_length=5000)
    description = models.TextField(null=True, blank=True)
    strategy = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=5000)


class CustomTier(BusinessTierModel):
    pass


class Tier1(BusinessTierModel):
    pass


class Tier2(BusinessTierModel):
    pass


class Tier3(BusinessTierModel):
    pass


class Tier4(BusinessTierModel):
    pass


class NonReportingTradeline(BusinessTierModel):
    pass


class CurrentTradelines(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    business_name = models.CharField(max_length=500)
    product = models.CharField(max_length=500)
    amount = models.CharField(max_length=500)
    tradeline_credit_amount = models.CharField(max_length=500)
    reports_to = models.CharField(max_length=500)
    we_can_help = models.BooleanField(null=True, default=True)
    recommended = models.BooleanField(null=True, default=True)


class CredibilitySteps(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    business_name = models.CharField(max_length=500)
    business_address = models.CharField(max_length=500)
    entity = models.BooleanField(default=False)
    ein = models.BooleanField(default=False)
    four11 = models.BooleanField(default=False)
    website = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    license = models.BooleanField(default=False)
    bankaccount = models.BooleanField(default=False)
    merchant = models.BooleanField(default=False)


class OtherChecklistSteps(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    established = models.BooleanField(default=False)
    tier1 = models.BooleanField(default=False)
    tier2 = models.BooleanField(default=False)
    tier3 = models.BooleanField(default=False)
    tier4 = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)

class NavigationLinks(models.Model):
    class Meta:
        db_table = "navigation_link"
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    is_main_site = models.BooleanField(default=False)
    is_every_site = models.BooleanField(default=False)
    is_whitelabel_site = models.BooleanField(default=False)

    def __str__(self):
        return self.name.capitalize()   
    
@receiver(pre_save, sender=NavigationLinks)
def check_navigtion_link(sender, instance, **kwargs):
    parsed = urlparse(instance.link)
    if parsed.scheme == '':
        instance.link = 'https://' + instance.link

class PageData(models.Model):
    class meta:
        db_table = "business_page_data"

    column_1 = models.CharField(max_length=50, default='', blank=True)
    column_2 = models.CharField(max_length=50, default='', blank=True)
    column_3 = models.CharField(max_length=50, default='', blank=True)
    column_4 = models.CharField(max_length=50, default='', blank=True)
    column_5 = models.CharField(max_length=50, default='', blank=True)
    column_6 = models.CharField(max_length=200, default='', blank=True)

    def convert_to_url(self, field):
        parsed = urlparse(field)
        if parsed.scheme == '':
            return 'https://' + field
        else:
            return field

    def __str__(self):
        return f"{self.column_1}, {self.column_2}, ..."

@receiver(pre_save, sender=PageData)
def check_navigtion_link(sender, instance, **kwargs):
    if instance.column_1 and not instance.column_2:
        instance.column_1 = instance.convert_to_url(instance.column_1)
    elif instance.column_2 and not instance.column_3:
        instance.column_2 = instance.convert_to_url(instance.column_2)
    elif instance.column_3 and not instance.column_4:
        instance.column_3 = instance.convert_to_url(instance.column_3)
    elif instance.column_4 and not instance.column_5:
        instance.column_4 = instance.convert_to_url(instance.column_4)
    elif instance.column_5 and not instance.column_6:
        instance.column_5 = instance.convert_to_url(instance.column_5)
    else:
        instance.column_6 = instance.convert_to_url(instance.column_6)


class Page(models.Model):
    class meta:
        db_table = "business_page"
    
    name = models.CharField(max_length=200)
    video = models.CharField(max_length=100)

    is_main_site = models.BooleanField(default=False)
    is_every_site = models.BooleanField(default=False)
    is_whitelabel_site = models.BooleanField(default=False)

    column_name_1 = models.CharField(max_length=50, default='', blank=True)
    column_name_2 = models.CharField(max_length=50, default='', blank=True)
    column_name_3 = models.CharField(max_length=50, default='', blank=True)
    column_name_4 = models.CharField(max_length=50, default='', blank=True)
    column_name_5 = models.CharField(max_length=50, default='', blank=True)
    column_name_6 = models.CharField(max_length=50, default='', blank=True)
    
    data = models.ManyToManyField("PageData", blank=True)

    def __str__(self):
        return self.name.capitalize()   


