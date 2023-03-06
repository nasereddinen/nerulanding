from dynamic.models import *
from yourplan.models import *

plans = {
    "sezzle": Sezzle,
    "klarna": Klarna,
    "viabill": Viabill,
    "regularpayment": RegularPayment,
    "paypal": Paypal,
    "quadpay": Quadpay,
    "affirm": Affirm,
    "behalf": Behalf,
    "fundboxpay": FundBoxPay,
    "invoicefactoringpayment": InvoiceFactoringPayment,
    "stripe": Stripe,
}


def ProfileProcessor(request):
    try:
        user = Profile.objects.get(user=request.user)

        for i, k in plans.items():
            if k.objects.filter(user=user).count() > 0:
                return {'on_payment_plan': True}
    except Exception:
        pass
    return {}





def whitelabel_processor(request):
    obj = Subdomain.objects.filter(sub_name__exact=request.host.name).first()

    if not request.user.is_anonymous:
        # portal_count = Profile.objects.get(user=request.user).count()
        portal_count = 1
    else:
        portal_count = 0

    print("CONTEXT: ", request.host)

    if obj:
        return {
            'dynamic': obj,
            'why_buy_video': 'https://www.youtube.com/embed/bM8A5BDZglk',
            'iswhitelabeladmin': bool(portal_count),
        }
    else:
        return {

            'iswhitelabeladmin': bool(portal_count),
            'why_buy_video': 'https://www.youtube.com/embed/el9irdyyWcQ',
            'dynamic': {
                'is_main_site': True,
                'show_index_white_label': True,

                'title': 'Get Dinero Today',
                # 'title': 'Holliday consulting',
                # 'title': 'Saw consulting',
                'androidApp': "https://play.google.com/store/apps/details?id=com.millennialbusinessbuilders.getdianotoday",
                'iphoneApp': "https://apps.apple.com/us/app/get-dinero-today/id1520722061",
                'chromeExt': "https://chrome.google.com/webstore/detail/get-dinero-today/nopllamladnpdgmgcfbnhdfpllpgpcgk",
                'email': " info@getdinerotoday.com",
                'phno': " 877-726-2604",
                'address': "1629 K St NW Suite 300, Washington, DC 20006",
                'why_buy_link': "https://www.youtube.com/embed/VaGu7EyHaVk",
                'appImage': "/static/images/iphonescreenshot.png",
                'sub_name': "",
                'primary_color': "#3D7BBF",
                'secondary_color': "#dee1e6",
                'accent_color': "#1c6ef9",
                'bg_color': "-webkit-linear-gradient(-30deg, #177b3f, #07231b)",
                'faq_page': 'https://businessbuilders.zendesk.com/hc/en-us/sections/360010349512-FAQ',
                'logo': {"url": '/static/images/logo.png'},
                # 'logo': {"url": '/static/images/logos/sawlogo.png'},
                # 'logo': {"url": '/static/images/logos/Attachment-1.png'},
                'is_paid': False,
                'portal_price': 00.00,
            }
        }
