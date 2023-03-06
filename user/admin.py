from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ExportMixin

from .models import Portal, PortalGoal, Profile, VirtualCard, UserData, NewUserCredentials, ExternalResourceCredentials

admin.site.site_header = "Get Dinero Today Admin"
admin.site.site_title = "Get Dinero Today"
admin.site.index_title = "Administration"


# admin.site.site_url = None
class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile__phone_number')


class UserAdmin(ExportMixin, DjangoAdmin):
    resource_class = UserResource
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    '''
        Admin View for Profile
    '''
    list_display = ("user", "phone_number", "fax_number_paid", "toll_free_number_paid", "website_creation_paid",
                    "virtual_access_card_paid", 'whitelabel_portal','created_by')
    # fields = [
    #     "user", "phone_number", "fax_number_paid", "toll_free_number_paid", "website_creation_paid",
    #     "virtual_access_card_paid", "whitelabel_portal",
    # ]
    list_filter = ("fax_number_paid", "toll_free_number_paid", "website_creation_paid", "virtual_access_card_paid",'whitelabel_portal')
    search_fields = ('user__first_name', "user__last_name")
    readonly_fields = ('stripe_id',)


admin.site.register(Profile, ProfileAdmin)


class VirtualCardAdmin(admin.ModelAdmin):
    '''
        Admin View for VirtualCard
    '''
    list_display = ("user", "card_number", "mm_yy", "cvc", "zip_code",)
    list_filter = ('zip_code',)
    search_fields = ('user__username', "user__email", 'zip_code', 'card_number')


admin.site.register(VirtualCard, VirtualCardAdmin)


class PortalAdmin(admin.ModelAdmin):
    '''
        Admin View for Portal
    '''
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Portal, PortalAdmin)


class PortalGoalAdmin(admin.ModelAdmin):
    '''
        Admin View for PortalGoal
    '''
    list_display = ("name", "profile",)
    list_filter = ('profile',)
    search_fields = ("name", "profile_user__first_name", "profile_user__last_name")
    filter_horizontal = ["portals", ]


admin.site.register(PortalGoal, PortalGoalAdmin)


class UserDataAdmin(admin.ModelAdmin):
    '''
        Admin View for PortalGoal
    '''
    # list_display = ("name",)
    # list_filter = ('profile',)
    # search_fields = ("name", "profile_user__first_name", "profile_user__last_name")
    # filter_horizontal = ["portals", ]


admin.site.register(UserData, UserDataAdmin)



class UserCredsAdmin(admin.ModelAdmin):
    '''
        Admin View for PortalGoal
    '''
    # list_display = ("name",)
    # list_filter = ('profile',)
    # search_fields = ("name", "profile_user__first_name", "profile_user__last_name")
    # filter_horizontal = ["portals", ]


admin.site.register(NewUserCredentials, UserCredsAdmin)
admin.site.register(ExternalResourceCredentials, admin.ModelAdmin)


