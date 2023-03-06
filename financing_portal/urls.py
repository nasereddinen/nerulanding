from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'financing_portal'
urlpatterns = [
    url('^$', login_required(FinancingPortalHomeView.as_view(), login_url='/user/login'), name='financing-portal-home'),
    url('^purchase_products', login_required(FinancingPortalPurchaseProductsView.as_view(), login_url='/user/login'), name='purchase-products'),
    url('^payments', login_required(FinancingPortalPaymentsView.as_view(), login_url='/user/login'), name='payments'),
    url('^products_purchased', login_required(FinancingPortalProductsPurchasedView.as_view(), login_url='/user/login'), name='products-purchased'),
    url('^access_software', login_required(FinancingPortalAccessSoftware.as_view(), login_url='/user/login'), name='products-access'),
]
