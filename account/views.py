from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import login
from django.contrib import messages
from django.http import HttpRequest



# Create your views here.


def manage_account_view(request):
    return render(request, 'account/manage_account.html')

def login_view(request, *args, **kwargs):
    url_path = request.path
    next_query = request.POST.get('next')
    if next_query:
        if 'blog' in next_query: 
            post_id = next_query.split('/')
            post_id = int(post_id[2])
            login(request)
            if not request.user.is_authenticated:
                # if login was not successfull show message and reload current page
                messages.error(request, 'The username and/or password you specified are not correct.')
                return redirect(url_path + '?next=' + next_query)

            # if user login was successfull go to previous blog page
            full_blog_url = reverse('blog:single', kwargs={'pid':post_id})
            return redirect(full_blog_url)
                
        # if there is other next query parameter that we dont care
        # login and redirect to index page
        login(request)
        return redirect('/')
    
    else:
        # pure login url
        return login(request)
