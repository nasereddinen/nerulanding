from django import forms

from dynamic.models import Subdomain



class WhiteLabelForm(forms.ModelForm):
    logo = forms.ImageField(required=False)

    class Meta:
        model = Subdomain
        exclude = [
            'is_payment_done',
            'sub_name',
            'admins',
            'show_becoming_whitelabel_partner',
            'offer_paid_whitelabel',
            'appImage',
            'iphoneApp',
            'androidApp',
            'chromeExt',
            'extensionVideo',
            'affiliate_link',
            'whitelabelpartner_link',
            'show_free_access_to_affiliate_program',
            'whitelabel_index_video',
            'is_main_site',
            'faq_page',
            'is_paid_for_whitelabel',
            'can_edit'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.can_edit:
            self.fields.pop('primary_color')
            self.fields.pop('secondary_color')
            self.fields.pop('accent_color')
            self.fields.pop('bg_color')
            self.fields.pop('favicon')
            self.fields.pop('logo')
            self.fields.pop('seo_description')
            self.fields.pop('frontpage_text')
            self.fields.pop('aboutus_text')
