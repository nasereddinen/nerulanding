from business.views import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from business.urls import urlpatterns as business_urls


app_name = 'real_estate'

urlpatterns = [
    url('^$', login_required(BusinessHomePage.as_view(), login_url='/user/login'), name='homepage'),
] + business_urls[:-1]
