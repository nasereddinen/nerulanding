from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'marketingcourse'
urlpatterns = [

    url('roi', login_required(RoiView.as_view(), login_url='/user/login'),
        name='roi'),
    url('ltv', login_required(LtvView.as_view(), login_url='/user/login'),
        name='ltv'),
    url('cpa', login_required(CpaView.as_view(), login_url='/user/login'),
        name='cpa'),
    url('googler', login_required(GooglerView.as_view(), login_url='/user/login'),
        name='googler'),
    url('mainfile', login_required(MainFileView.as_view(), login_url='/user/login'),
        name='mainfile'),
    url('youtube', login_required(YoutubeView.as_view(), login_url='/user/login'),
        name='youtube'),
    url('facebook', login_required(FacebookView.as_view(), login_url='/user/login'),
        name='facebook'),
    url('facebookr', login_required(FacebookrView.as_view(), login_url='/user/login'),
        name='facebookr'),
    url('seo', login_required(SeoView.as_view(), login_url='/user/login'),
        name='seo'),
    url('googleads', login_required(GoogleadsView.as_view(), login_url='/user/login'),
        name='googleads'),
    url('coupons', login_required(CouponsView.as_view(), login_url='/user/login'),
        name='coupons'),    
]
