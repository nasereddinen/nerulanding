"""getdinerotoday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.static import serve
import debug_toolbar


from .views import *

urlpatterns = [
    path('api/', include('restapi.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('bcbsoftwares/', include('bcbsoftwares.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('business/', include('business.urls')),
    path('banking/', include('banking.urls')),
    path('cannabis/', include('portals.cannabis.urls')),
    path('loanportal/', include('loanportal.urls')),
    path('marketingcourse/', include('marketingcourse.urls')),
    path('businesscreditcourse/', include('businesscreditcourse.urls')),
    path('fitness/', include('portals.fitness.urls')),
    path('insurance_agent/', include('portals.insurance_agent.urls')),
    path('musician/', include('portals.musician.urls')),
    path('restaurant_catering/', include('portals.restaurant_catering.urls')),
    path('wedding_planner/', include('portals.wedding_planner.urls')),
    path('accountant/', include('portals.accountant.urls')),
    path('credit_repair/', include('portals.credit_repair.urls')),
    path('construction/', include('portals.construction.urls')),
    path('hair_salon/', include('portals.hair_salon.urls')),
    path('lawyer/', include('portals.lawyer.urls')),
    path('photography/', include('portals.photography.urls')),
    path('transportation/', include('portals.transportation.urls')),
    path('automotive/', include('portals.automotive.urls')),
    path('ecommerce/', include('portals.ecommerce.urls')),
    path('handy_man/', include('portals.handy_man.urls')),
    path('medical/', include('portals.medical.urls')),
    path('real_estate/', include('portals.real_estate.urls')),
    path('trucking/', include('portals.trucking.urls')),
    path('yourplan/', include('yourplan.urls')),
    path('creditcourse/', include('creditcourse.urls')),
    path('covid19/', include('covid19.urls')),
    path('affiliate/', include('affiliate.urls')),
    path('goals/', include('goals.urls')),
    path('products/', include('products.urls')),
    path('onlinetools/', include('onlinetools.urls')),
    path('freewhitelabelprogramonboarding/',
         include('freewhitelabelprogramonboarding.urls')),
    path('whitelabelpartnerportal/', include('whitelabelpartnerportal.urls')),
    path('chromeextension/', include('chromeextension.urls')),
    path('onboarding/', include('onboarding.urls')),
    path('financing_portal/', include('financing_portal.urls')),

    url('dashboard/', login_required(HomePage.as_view(),
        login_url='/user/login'), name='homepage'),
    url('about-us/', AboutUsView.as_view(), name='about-us'),
    url('pricing/', PricingView.as_view(), name='pricing'),
    url('services/', ServicesView.as_view(), name='services'),
    url('financing/', FinancingView.as_view(), name='financing'),
    url('webinar/', WebinarView.as_view(), name='webinar'),
    url('webinaroffer/', WebinarOfferView.as_view(), name='webinaroffer'),
    url('partner/', PartnerView.as_view(), name='partner'),
    url('contact/', ContactView.as_view(), name='contact'),
    url('customersuccessagent/', CustomerSuccessAgentView.as_view(),
        name='customersuccessagent'),
    url('whitelabel/', WhiteLabelView.as_view(), name='whitelabel'),
    url('affiliate_program/', AffiliatelView.as_view(), name='affiliate'),
    url('faq/', FAQView.as_view(), name='faq'),
    url('testimonial/', TestimonialsView.as_view(), name='testimonial'),
    url('^$', IndexView.as_view(), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
