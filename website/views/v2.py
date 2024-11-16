# views are class based.

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages

from website.forms import ContactForm

class ContactViewFormView(FormView):
    form_class = ContactForm
    template_name = 'website/contact.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, "Message Sent")
        form.save()
        return super().form_valid(form)


class AboutViewTemplateView(TemplateView):
    template_name = 'website/about.html'



# TODO: add functionlity that logged in users info
#  gets into form fields or only logged in can send message.