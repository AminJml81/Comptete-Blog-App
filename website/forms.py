from django import forms
from website.models import Contact
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
# from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    # using captch version2(simple captcha) for contact form
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    #captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'