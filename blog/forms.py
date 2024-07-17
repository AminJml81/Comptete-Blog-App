from blog.models import Comment
from django import forms

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class CommentForm(forms.ModelForm):
    # using captch version2(simple captcha) for contact form
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Comment
        fields = ['message',]
