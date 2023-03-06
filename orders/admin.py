from django.apps import apps
from django.contrib import admin

from .models import TradelineOrder, UserSteps

app = apps.get_app_config('orders')


class TradelineOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'tradeline', 'whitelabel_portal')


admin.site.register(TradelineOrder, TradelineOrderAdmin)


class UserStepsAdmin(admin.ModelAdmin):
    list_display = ('user', 'whitelabel_portal')


admin.site.register(UserSteps, UserStepsAdmin)
