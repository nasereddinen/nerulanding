from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'products'
urlpatterns = [

    url('dnbproducts', login_required(DnbProductsView.as_view(), login_url='/user/login'),
        name='dnbproducts'),
]
