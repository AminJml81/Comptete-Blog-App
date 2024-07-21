from blog.models import Comment
from django import forms

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    # using captch version2(simple captcha) for contact form
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['message',]
