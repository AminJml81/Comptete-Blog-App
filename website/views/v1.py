# views are function based.

from django.shortcuts import render
from django.contrib import messages

from website.forms import ContactForm
# Create your views here.

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Message Sent")
            form.save()
        else:
            messages.error(request, "Captcha Is Required")
        
    form = ContactForm()
    context = {'form': form}
    return render(request, 'website/contact.html', context)

def about_view(request):
    return render(request, 'website/about.html')