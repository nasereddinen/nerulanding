from django.apps import apps
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from products.services import create_usersteps_for_subdomain
from .models import Subdomain

# Register your models here.

app = apps.get_app_config('dynamic')


class SubdomainResource(resources.ModelResource):
    class Meta:
        model = Subdomain
        fields = ('sub_name', 'phno')
        force_init_instance = True

    def before_import_row(self, row, row_number=None, **kwargs):
        all_names = list(Subdomain.objects.values_list('sub_name', flat=True))

        count = 1
        while row['sub_name'] in all_names:
            row['sub_name'] = row['sub_name'] + str(count)
            count += 1
        row['sub_name'] = row['sub_name'] + 'businessbuilders'
        row['sub_name'] = row['sub_name'].lower().replace(" ", "")


class SubdomainAdmin(ImportExportModelAdmin):
    list_display = ('sub_name', 'is_payment_done', 'webinar',
                    'iphoneApp', 'androidApp', 'chromeExt',
                    'homeVideo', 'email', 'title', 'address',
                    'phno', 'logo', 'why_buy_link', 'appImage',
                    'primary_color', 'secondary_color',
                    'accent_color', 'bg_color')
    filter_horizontal = ('admins',)
    search_fields = ()
    actions = ['create_user_steps', 'payment_done', 'default_appimage', 'default_email', 'default_links', 'default_colors']
    resource_class = SubdomainResource

    def create_user_steps(self, request, queryset):
        for subdomain in queryset:
            create_usersteps_for_subdomain(subdomain)

    def payment_done(self, request, queryset):
        for subdomain in queryset:
            subdomain.is_payment_done = True
            subdomain.save()

    def default_appimage(self, request, queryset):
        for subdomain in queryset:
            subdomain.appImage = '/static/images/thebusinessbuildersapp.png'
            subdomain.save()

    def default_email(self, request, queryset):
        for subdomain in queryset:
            subdomain.email = 'info@businesscreditbuildersllc.com'
            subdomain.save()

    def default_links(self, request, queryset):
        for subdomain in queryset:
            subdomain.webinar = 'https://youtu.be/xNCfnbGT5hY'
            subdomain.iphoneApp = 'https://apps.apple.com/us/app/the-business-credit-builders/id1528895728'
            subdomain.androidApp = 'https://play.google.com/store/apps/details?id=com.millennialbusinessbuilders.businesscreditbuilders'
            subdomain.chromeExt = 'https://chrome.google.com/webstore/detail/the-business-credit-build/jpbbaabmhfpfdjnomgdieempedlaelfi'
            subdomain.homeVideo = 'https://youtu.be/xNCfnbGT5hY'
            subdomain.extensionVideo = 'https://www.youtube.com/watch?v=Z1HK9uSOMCI'
            subdomain.save()

    def default_colors(self, request, queryset):
        for subdomain in queryset:
            subdomain.primary_color = '#916e06'
            subdomain.secondary_color = '#fffff'
            subdomain.accent_color = '#115d22'
            subdomain.bg_color = '#333333'
            subdomain.login_window_color = '#ffffff'
            subdomain.save()

    create_user_steps.short_description = "Create user steps"
    payment_done.short_description = "Make Payment Done"
    payment_done.default_appimage = "Set Default App Image"
    payment_done.default_email = "Set Default Email"
    payment_done.default_links = "Set Default Links"
    payment_done.default_colors = "Set Default Colors"


admin.site.register(Subdomain, SubdomainAdmin)
