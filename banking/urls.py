from django.urls import path
from . import views


urlpatterns = [
  path('',views.Index,name='banking_home'),
  path('about/',views.About,name='banking_about'),
  path('contact/',views.Contact,name='banking_contact'),
  path('faq/',views.Faq,name='banking_faq'),
  path('pricing/',views.Pricing,name='banking_pricing'),
  path('privacy-policy/',views.PrivacyPolicy,name='banking_privacy-policy'),
  path('services/',views.Services,name='banking_services'),
  path('terms-of-service/',views.TermsOfService,name='banking_terms-of-service'),
]