from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import login
from django.contrib import messages
from django.http import HttpResponseRedirect



# Create your views here.


def manage_account_view(request):
    return render(request, 'account/manage_account.html')

def login_view(request, *args, **kwargs):
    next_url = request.POST.get('next')
    if next_url:
        if 'blog' in next_url: 
            post_id = next_url.split('/')
            post_id = int(post_id[2])
            login(request)
            next_url = reverse('blog:single', kwargs={'pid':post_id})
            if not request.user.is_authenticated:
                messages.error(request, 'The username and/or password you specified are not correct.')
                return HttpResponseRedirect(request.path_info)

            return redirect(next_url)
                
        
        login(request)
        return redirect('/')
    else:
        return login(request)
