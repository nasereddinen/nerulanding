from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from services.StripeService import StripeService


class ProfileUserManager(models.Manager):
    def create_user(self, email, password, first_name, last_name, phone_number, whitelabel_portal=None,created_by='Signup-page'):
        stripe_user = StripeService.create_user(first_name=first_name, last_name=last_name, email=email)
        user = User.objects.create_user(email=email, username=email, password=password, first_name=first_name,
                                        last_name=last_name)
        profile = Profile(user=user, phone_number=phone_number, stripe_id=stripe_user['id'],
                          whitelabel_portal=whitelabel_portal,created_by=created_by)
        profile.save()
        return profile


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=500, null=True)
    is_partner = models.BooleanField(default=False)
    updates_made = models.CharField(max_length=500, null=True, default="N/A")
    residual_amount = models.CharField(max_length=500, null=True, default="N/A")
    expected_payout = models.CharField(max_length=500, null=True, default="N/A")
    fax_number_paid = models.BooleanField(default=False)
    toll_free_number_paid = models.BooleanField(default=False)
    website_creation_paid = models.BooleanField(default=False)
    virtual_access_card_paid = models.BooleanField(default=False)
    created_by = models.CharField(max_length=500, null=True,blank=True, default="Signup-page")
    whitelabel_portal = models.CharField(max_length=200, null=True, blank=True)

    can_see_only_created_portals = models.BooleanField(default=False)

    what_is_done = models.TextField(blank=True)
    what_is_left = models.TextField(blank=True)
    what_is_purchased = models.TextField(blank=True)
    what_is_recommended = models.TextField(blank=True)
    user_goals_text = models.TextField(blank=True)

    available_credit_limit = models.DecimalField(max_digits=100, default=1500, decimal_places=2)
    credit_line = models.DecimalField(max_digits=100, default=1000, decimal_places=2)

    stripe_id = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    objects = ProfileUserManager()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "1. Profile"
        verbose_name_plural = "1. Profiles"


class VirtualCard(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='virtual_card', null=True)
    card_number = models.CharField("Card Number", max_length=20)
    mm_yy = models.CharField("MM/YY", max_length=50)
    cvc = models.CharField("CVC", max_length=3)
    zip_code = models.CharField("Zip Code", max_length=50)

    class Meta:
        verbose_name = "2. Virtual Card"
        verbose_name_plural = "2. Virtual Cards"

    def __str__(self):
        return self.card_number


class Portal(models.Model):
    name = models.CharField("Portal Name", max_length=255)
    code = models.CharField("Unique portal code", max_length=50, null=True, unique=True)

    class Meta:
        verbose_name = "3. Portal"
        verbose_name_plural = "3. Portals"

    def __str__(self):
        return self.name


class PortalGoal(models.Model):
    name = models.CharField("Custom portal name", max_length=50, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=200, blank=True, null=True)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='portal_goals')
    portals = models.ManyToManyField("Portal")

    class Meta:
        verbose_name = "4. Portal Goal"
        verbose_name_plural = "4. Portal Goals"

    def __str__(self):
        return "{}-portals-goals".format(self.profile)

    def get_absolute_url(self):
        if not self.slug:
            self.save()
        return reverse("user:portal_goals", kwargs={"slug": self.slug})


class UserData(models.Model):
    class Meta:
        verbose_name = "5. Personal Information"
        verbose_name_plural = "5. Personal Information"

    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    duns = models.CharField("DUNS Number", null=True, blank=True, max_length=255)
    ein = models.CharField("EIN number", null=True, max_length=255)

    first_name = models.CharField("First Name", null=True, max_length=255)
    last_name = models.CharField("Last Name", null=True, max_length=255)

    personal_street_address_1 = models.CharField("Personal Address Line 1", null=True, max_length=255)
    personal_street_address_2 = models.CharField("Personal Address Line 2", null=True, blank=True, max_length=255)
    personal_zip_code = models.CharField("Personal Zip Code", null=True, max_length=255)
    personal_city = models.CharField("Personal City", null=True, max_length=255)
    personal_state = models.CharField("Personal State", null=True, max_length=255)
    personal_country = models.CharField("Personal Country", null=True, max_length=255)
    personal_phone = models.CharField("Personal Phone", null=True, max_length=255)

    billing_street_address_1 = models.CharField("Billing Address Line 1", null=True, blank=True, max_length=255)
    billing_street_address_2 = models.CharField("Billing Address Line 2", null=True, blank=True, max_length=255)
    billing_zip_code = models.CharField("Billing Zip Code", null=True, blank=True, max_length=255)
    billing_city = models.CharField("Billing City", null=True, blank=True, max_length=255)
    billing_state = models.CharField("Billing State", null=True, blank=True, max_length=255)
    billing_country = models.CharField("Billing Country", null=True, blank=True, max_length=255)
    billing_phone = models.CharField("Billing Phone", null=True, blank=True, max_length=255)

    business_name = models.CharField("Business Name", null=True, max_length=255)

    business_street_address_1 = models.CharField("Business Address Line 1", null=True, max_length=255)
    business_street_address_2 = models.CharField("Business Address Line 2", null=True, blank=True, max_length=255)
    business_zip_code = models.CharField("Business Zip Code", null=True, max_length=255)
    business_city = models.CharField("Business City", null=True, max_length=255)
    business_state = models.CharField("Business State", null=True, max_length=255)
    business_country = models.CharField("Business Country", null=True, max_length=255)
    business_phone = models.CharField("Business Phone", null=True, max_length=255)

    email = models.CharField("Email Address", null=True, max_length=255)

    website = models.CharField("Website", null=True, blank=True, max_length=255)
    toll_free_number = models.CharField("Toll Free Number", blank=True, null=True, max_length=255)
    fax_number = models.CharField("Fax Number", null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if self.first_name == "":
            self.first_name = self.user.user.first_name
        if self.last_name == "":
            self.last_name = self.user.user.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name} personal details"


class NewUserCredentials(models.Model):
    email = models.CharField("email", max_length=100, null=True)
    password = models.CharField("Password", max_length=100, null=True)

    class Meta:
        verbose_name = "7. New Users"
        verbose_name_plural = "7. New Users"

    def __str__(self):
        return self.email


class ExternalResourceCredentials(models.Model):
    class Meta:
        verbose_name = "8. External Credential"
        verbose_name_plural = "8. External Credentials"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='external_resources')
    name = models.CharField(blank=True, null=True, max_length=50)
    url = models.URLField(blank=True, null=True, max_length=100)
    login = models.CharField(blank=True, null=True, max_length=50)
    password = models.CharField(blank=True, null=True, max_length=50)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.user.username}"
