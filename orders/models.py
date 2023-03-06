from datetime import datetime

from django.conf import settings
from django.db import models

from business.models import Tier1, Tier2, Tier3, Tier4, CustomTier, NonReportingTradeline
from dynamic.models import Subdomain
from products.models import Tradelines
from user.models import Profile


class TradelineOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    which = models.IntegerField(default=0)
    tradeline = models.ForeignKey(Tradelines, null=True, blank=True, on_delete=models.CASCADE)
    tradeline_tier1 = models.ForeignKey(Tier1, null=True, blank=True, on_delete=models.CASCADE)
    tradeline_tier2 = models.ForeignKey(Tier2, null=True, blank=True, on_delete=models.CASCADE)
    tradeline_tier3 = models.ForeignKey(Tier3, null=True, blank=True, on_delete=models.CASCADE)
    tradeline_tier4 = models.ForeignKey(Tier4, null=True, blank=True, on_delete=models.CASCADE)
    non_reporting_tradeline = models.ForeignKey(NonReportingTradeline, null=True, blank=True, on_delete=models.CASCADE)
    custom_tier = models.ForeignKey(CustomTier, null=True, blank=True, on_delete=models.CASCADE)
    whitelabel_portal = models.ForeignKey(Subdomain, on_delete=models.SET_NULL, null=True)
    last_purchased = models.DateField(auto_now_add=True, null=True, blank=True)
    screenshot = models.CharField(max_length=200, null=True, blank=True)
    expected_time = models.DateField(default=datetime.now, null=True, blank=True)

    class Meta:
        verbose_name = "1. Tradeline Order"
        verbose_name_plural = "1. Tradeline Orders"


class UserSteps(models.Model):
    _choices = (
        (1, "Not ordered"),
        (2, "In progress"),
        (3, "Done"),
    )

    STEPS_OFFER = (
        (1, "Not Ordered"),
        (2, "Ordered"),
        (3, "Done"),
    )

    _industry_choices = (
        (1, "Electrician"),
        (2, "Gardener"),
        (3, "Tattoo Artist"),
        (4, "Photography"),
        (5, "Limo Service"),
        (6, "Nutrition Advisor"),
        (7, "Life Coach"),
        (8, "Veterinary clinic"),
        (9, "Laundromat"),
        (10, "Fitness Club"),
        (11, "Dentist"),
        (12, "Consulting"),
        (13, "Auto Repair"),
        (14, "Tutor"),
        (15, "Bakery"),
        (16, "Financial Advisor"),
        (17, "Lawyer"),
        (18, "Marketing Agency"),
        (19, "Trucking"),
        (20, "Locksmith"),
        (21, "Medical Clinic"),
        (22, "Dance Studio"),
        (23, "Carpenter"),
        (24, "Moving Company"),
        (25, "Hair Salon"),
        (26, "Cleaning Service"),
        (27, "Car Dealer"),
        (28, "Portfolio"),
        (29, "Real Estate"),
        (30, "Preschool"),
        (31, "Spa Service"),
        (32, "Physical Therapist"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    email = models.CharField("User Email", max_length=500, null=False)
    first_name = models.CharField("First Name", max_length=500, null=True)
    last_name = models.CharField("Last Name", max_length=500, null=True)
    phone = models.CharField("Phone Number", max_length=500, null=True)

    website = models.IntegerField("Website", choices=_choices, null=True, default=1)
    industry_name = models.IntegerField("Industry", choices=_industry_choices, null=True, default=1, blank=True)

    toll_free_number = models.IntegerField("Toll free number", choices=_choices, null=True, default=1)
    fax_number = models.IntegerField("Fax number", choices=_choices, null=True, default=1)
    domain = models.IntegerField("Domain", choices=_choices, null=True, default=1)
    professional_email_address = models.IntegerField("Professional email", choices=_choices, null=True, default=1)
    business_builder_program = models.IntegerField("Business Builder Program", choices=_choices, null=True, default=1)

    base_professional_mailing_address = models.CharField("Base professional mailing address", null=True, default='',
                                                         blank=True, max_length=500)

    domain_name = models.CharField("Domain name", null=True, default='', blank=True, max_length=500)

    fax_number_act = models.CharField("Actual fax number", null=True, default='', blank=True, max_length=500)
    toll_free_number_act = models.CharField("Actual toll free number", null=True, default='', blank=True,
                                            max_length=500)

    professional_email_address_act = models.CharField("Actual professional email address", null=True, default='',
                                                      blank=True, max_length=500)
    website_act = models.CharField("Actual website link", null=True, default='', blank=True, max_length=500)
    domain_act = models.CharField("Actual domain name", null=True, default='', blank=True, max_length=500)

    domain_dashboard = models.CharField("Domain name dashboard", null=True, default='', blank=True, max_length=500)
    email_provider = models.CharField("Email provider", null=True, default='', blank=True, max_length=500)

    toll_free_username = models.CharField("Toll Free Number username", null=True, default='', blank=True,
                                          max_length=500)
    toll_free_password = models.CharField("Toll Free Number password", null=True, default='', blank=True,
                                          max_length=500)
    toll_free_number_prefix = models.CharField("Toll Free prefix", null=True, default='', blank=True, max_length=500)
    toll_free_quantity = models.CharField("Toll Free amount", null=True, default='', blank=True, max_length=500)
    fax_number_prefix = models.CharField("Fax number prefix", null=True, default='', blank=True, max_length=500)
    fax_number_quantity = models.CharField("Fax amount amount", null=True, default='', blank=True, max_length=500)

    website_username = models.CharField("Website username", null=True, default='', blank=True, max_length=500)
    website_password = models.CharField("Website password", null=True, default='', blank=True, max_length=500)

    domain_username = models.CharField("Domain username", null=True, default='', blank=True, max_length=500)
    domain_password = models.CharField("Domain password", null=True, default='', blank=True, max_length=500)

    email_username = models.CharField("Email username", null=True, default='', blank=True, max_length=500)
    email_password = models.CharField("Email password", null=True, default='', blank=True, max_length=500)

    whitelabel_portal = models.ForeignKey(Subdomain, on_delete=models.SET_NULL, null=True, blank=True)

    # STEPS_TO_DO:
    LLC = models.IntegerField("LLC", choices=STEPS_OFFER, null=True, default=1)
    EIN = models.IntegerField("EIN", choices=STEPS_OFFER, null=True, default=1)
    business_account = models.IntegerField("Business Account", choices=STEPS_OFFER, null=True, default=1)
    merchant_account = models.IntegerField("Merchant Account", choices=STEPS_OFFER, null=True, default=1)
    duns = models.IntegerField("DUNS", choices=STEPS_OFFER, null=True, default=1)
    tradelines = models.IntegerField("tradelines", choices=STEPS_OFFER, null=True, default=1)
    marketing = models.IntegerField("marketing", choices=STEPS_OFFER, null=True, default=1)

    class Meta:
        verbose_name = "2. User Steps"
        verbose_name_plural = "2. User steps"

    def __str__(self):
        return f"{self.email} steps"
