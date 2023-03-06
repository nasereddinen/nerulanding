from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

app_name = 'affiliate'
urlpatterns = [
        url('^$', login_required(HomeAffiliateView.as_view(), login_url='/user/login'),
            name='home-affiliate'),
    url('myresiduals', login_required(MyResidualsView.as_view(), login_url='/user/login'),
        name='myresiduals'),
    url('affiliate-enternewleads', login_required(EnterNewLeadsView.as_view(), login_url='/user/login'),
        name='affiliate-enternewleads'),
    path('create-new-lead', login_required(LeadCreateView.as_view()), name='add_new_lead'),
    path('leadoverview/edit/<int:pk>', lead_update, name='lead_edit'),
    path('addbankinfo/edit/<int:pk>', bank_info_update, name='paypal_info_update'),
    path('addpaypalinfo/edit/<int:pk>', paypal_info_update, name='bank_info_update'),
    url('leadoverview', login_required(LeadOverviewView.as_view(), login_url='/user/login'),
        name='leadoverview'),
    url('mysales', login_required(MySalesView.as_view(), login_url='/user/login'),
        name='mysales'),
    url('networkmarketing', login_required(NetworkMarketingView.as_view(), login_url='/user/login'),
        name='networkmarketing'),
    url('addbankinfo_form', login_required(AddBankInfoFormView.as_view(), login_url='/user/login'),
        name='addbankinfo_form'),
    url('sharelinks', login_required(ShareLinksView.as_view(), login_url='/user/login'),
        name='sharelinks'),
    url('addbankinfo', login_required(AddBankInfoView.as_view(), login_url='/user/login'),
        name='addbankinfo'),
    url('addpaypalinfo_form', login_required(AddPaypalInfoFormView.as_view(), login_url='/user/login'),
        name='addpaypalinfo_form'),
    url('addpaypalinfo', login_required(AddPaypalInfoView.as_view(), login_url='/user/login'),
        name='addpaypalinfo'),
    url('commission', login_required(CommissionView.as_view(), login_url='/user/login'),
            name='commission'),
]
