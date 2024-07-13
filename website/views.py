from django.shortcuts import render
from django.contrib import messages

from website.forms import ContactForm
# Create your views here.

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Captcha Is Required")
        
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def about_view(request):
    return render(request, 'about.html')