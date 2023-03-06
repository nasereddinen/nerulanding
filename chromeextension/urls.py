from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ChromeExtensionIndexView
from business.urls import urlpatterns as business_urls


app_name = 'chromeextension'
urlpatterns = [

    url('^$', login_required(ChromeExtensionIndexView.as_view(), login_url='/user/login'),
        name='chromeextensionindex'),
] + business_urls[:-1]
