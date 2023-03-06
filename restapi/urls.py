from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .rest_views.business_views import StepsChecklistAPI, StepsChecklistCredibilityAPI, BusinessCreditBuilderTrackerAPI
from .rest_views.product_views import TradelinesProductsAPI, UserStepsProductsAPI, StripeOrderAPI, UserDataAPI
from .rest_views.whitelabel_views import ResidualsAPI, LeadsAPI, SalesAPI, SignedUsersAPI, OrdersAPI, InvoicesAPI, \
    PaymentsAPI, CreditsAPI, BankPaymentInformationAPI, PaypalInformationAPI, WhiteLabelLogoAPI, WhiteLabelUserLogoAPI
from .views import *

urlpatterns = [

    path('token/', TokenObtainPairPatchedView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('user/get_user_info/', GetUserByToken.as_view(), name='get_user_info'),
    path('user/fetch_personal_data/', FetchPersonalData.as_view(), name='fetch_personal_data'),
    path('user/register/', RegisterNewUserAPI.as_view(), name='register_new_user'),
    path('user/credit_steps/', GetUserStepsAPI.as_view(), name='fetch_steps_data'),

    path('business/sarter_vendor_list/', StarterVendorListAPI.as_view({'get': 'list'}), name='sarter_vendor_list'),
    path('business/store_credit_vendor_list/', StoreCreditVendorListAPI.as_view({'get': 'list'}), name='store_credit_vendor_list'),
    path('business/revolving_credit_vendor/', RevolvingBusinessCreditVendorAPI.as_view({'get': 'list'}), name='revolving_credit_vendor'),
    path('business/nopg/', NOPGAPI.as_view({'get': 'list'}), name='nopg'),

    path('business/personal_credit_card/', PersonalCreditCardAPI.as_view({'get': 'list'}), name='personal_credit_card'),
    path('business/business_credit_card/', BusinessCreditCardAPI.as_view({'get': 'list'}), name='business_credit_card'),
    path('business/short_term_loan/', ShortTermLoanAPI.as_view({'get': 'list'}), name='short_term_loan'),
    path('business/business_term_loan/', BusinessTermLoanAPI.as_view({'get': 'list'}), name='business_term_loan'),
    path('business/sba_loan/', SBALoanAPI.as_view({'get': 'list'}), name='sba_loan'),
    path('business/personal_loan/', PersonalLoanAPI.as_view({'get': 'list'}), name='personal_loan'),
    path('business/business_lines_of_credit/', BusinessLinesOfCreditAPI.as_view({'get': 'list'}),
         name='business_lines_of_credit'),
    path('business/no_credit_check_loan/', NoCreditCheckLoansAPI.as_view({'get': 'list'}), name='no_credit_check_loan'),
    path('business/invoice_factoring/', InvoiceFactoringAPI.as_view({'get': 'list'}), name='invoice_factoring'),
    path('business/invoice_financing/', InvoiceFinancingAPI.as_view({'get': 'list'}), name='invoice_financing'),
    path('business/equipment_financing/', EquipmentFinancingAPI.as_view({'get': 'list'}), name='equipment_financing'),

    path('business/checklist/', StepsChecklistAPI.as_view(), name='checklist'),
    path('business/credibilitycheck/', StepsChecklistCredibilityAPI.as_view(), name='checklistcredibility'),

    path('loans/upload-document/', uploadLoanDocument.as_view(), name='upload-document'),
    path('domain/check', checkDomainApi.as_view(), name='check_domain'),

    path('wt/residuals/', ResidualsAPI.as_view(), name='wt_myresiduals'),
    path('wt/leads/', LeadsAPI.as_view(), name='wt_leads'),
    path('wt/sales/', SalesAPI.as_view(), name='wt_sales'),
    path('wt/signedusers/', SignedUsersAPI.as_view(), name='wt_signedusers'),
    path('wt/orders/', OrdersAPI.as_view(), name='wt_orders'),
    path('wt/invoices/', InvoicesAPI.as_view(), name='wt_invoices'),
    path('wt/payments/', PaymentsAPI.as_view(), name='wt_payments'),
    path('wt/credits/', CreditsAPI.as_view(), name='wt_credits'),
    path('wt/bankpayments/', BankPaymentInformationAPI.as_view(), name='wt_bankpayments'),
    path('wt/paypalinfo/', PaypalInformationAPI.as_view(), name='wt_paypalinfo'),


    path('wt/getlogo/', WhiteLabelLogoAPI.as_view(), name='wt_logo'),
    path('wt/getuserlogo/', WhiteLabelUserLogoAPI.as_view(), name='wt_user_logo'),

    path('business/gettradelines/', TradelinesAPI.as_view(), name='get_tradelines'),
    path('business/getcredittracker/', BusinessCreditBuilderTrackerAPI.as_view(), name='credit_tracker'),



    path('products/tradelines/', TradelinesProductsAPI.as_view(), name='get_tradeline_products'),
    path('products/businesssteps/', UserStepsProductsAPI.as_view(), name='get_business_steps_products'),


    path('orders/stripeorder/', StripeOrderAPI.as_view(), name='stripe_order_products'),


    path('user/userpersonaldata/', UserDataAPI.as_view(), name='userpersonaldata'),


]