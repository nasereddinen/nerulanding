from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'onboarding'
urlpatterns = [

    url('onboardinghome', login_required(OnboardingView.as_view(), login_url='/user/login'),
        name='onboardinghome'),
    url('viewbusinesstradelines', login_required(BusinessTradelineView.as_view(), login_url='/user/login'),
        name='viewbusinesstradelines'),
    url('viewdomainanme', login_required(DomainNameView.as_view(), login_url='/user/login'),
        name='viewdomainname'),
    url('viewfaxnumber', login_required(FaxNumberView.as_view(), login_url='/user/login'),
        name='viewfaxnumber'),
    url('viewprofessionalemailaddress', login_required(EmailView.as_view(), login_url='/user/login'),
        name='viewprofessionalemailaddress'),
    url('viewsoftwarepurchases', login_required(SoftwarePurchaseView.as_view(), login_url='/user/login'),
        name='viewsoftwarepurchases'),
    url('viewtollfree', login_required(TollFreeView.as_view(), login_url='/user/login'),
        name='viewtollfree'),
    url('viewwebsite', login_required(WebsiteView.as_view(), login_url='/user/login'),
        name='viewwebsite'),
]
