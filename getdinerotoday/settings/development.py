from getdinerotoday.settings.settings import *
from dotenv import dotenv_values
config = dotenv_values(".env")

DEBUG = True

SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'

STRIPE_PUBLISHABLE_KEY = "pk_test_51MKgjLKFzQhQect9294CN3IcHjStYTzBdClmCzwj9MIgpJtosi1zzheiNzapSypmsBAgAurn2Agmu3dKBMG59B8w00InQKVNEq"
STRIPE_SECRET_KEY = "sk_test_51MKgjLKFzQhQect9gph7QiSZG91nheTyjLnaj5ZpJnlQb0GFeeLMwI0N3MEIqhUWL9JZ7TMuiCXPfSYUyjPSU6ny00ySFjmwG2"

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': True,
}
ALLOWED_HOSTS = ['*']
