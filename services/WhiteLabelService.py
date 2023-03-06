from dynamic.models import Subdomain
from financing_portal.models import Product
from products.models import Tradelines, UserStepsProduct
from user.models import Profile
from whitelabelpartnerportal.models import WholeSale


class WhiteLabelService:

    @classmethod
    def get_administrated_subdomains(cls, request):
        profile = Profile.objects.get(user=request.user)
        subdomains = Subdomain.objects.filter(admins__in=[profile])
        return subdomains

    @classmethod
    def get_subdomain_users(cls, subdomain):
        users = Profile.objects.filter(whitelabel_portal=subdomain)
        return users

    @classmethod
    def get_users_by_subdomains(cls, request):
        admin_subdomains = WhiteLabelService.get_administrated_subdomains(request)
        response = []
        for i in admin_subdomains:
            subdomain_users = {
                'sub_name': i,
                'users': WhiteLabelService.get_subdomain_users(i)
            }
            response.append(subdomain_users)
        return response

    @classmethod
    def get_tradelines_by_subdomain(cls, subdomain):
        tradelines = Tradelines.objects.filter(whitelabel_portal=subdomain)
        return tradelines

    @classmethod
    def get_usersteps_by_subdomain(cls, subdomain):
        usersteps = UserStepsProduct.objects.filter(whitelabel_portal=subdomain)
        return usersteps

    @classmethod
    def get_whitelabel_products(cls, request):
        subdomains = cls.get_administrated_subdomains(request)
        products_in_subdomains = []
        for subdomain in subdomains:
            products_in_subdomains.append({'subdomain': subdomain.sub_name,
                                           'tradelines': cls.get_tradelines_by_subdomain(subdomain),
                                           'softwares':  Product.objects.all(),
                                           'usersteps': cls.get_usersteps_by_subdomain(subdomain)})
        return products_in_subdomains
