from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'freewhitelabelprogramonboarding'
urlpatterns = [

    url('onboarding', login_required(OnboardingView.as_view(), login_url='/user/login'),
        name='onboarding'),
    url('whitelabelaccess', login_required(WhitelabelaccessView.as_view(), login_url='/user/login'),
        name='whitelabelaccess'),
    url('partner-resources', login_required(PartnerResourceView.as_view(),login_url='/user/login'),name='freewhitelabel-resource'),
    url('view-free-portals',login_required(ViewPortalsView.as_view(),login_url='/user/login'),name='freewhitelabel-portals')
]
