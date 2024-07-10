from django.shortcuts import render

from website.forms import ContactForm
# Create your views here.

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def about_view(request):
    return render(request, 'about.html')