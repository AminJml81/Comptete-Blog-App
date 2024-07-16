from django.shortcuts import render

# Create your views here.


def manage_account_view(request):
    return render(request, 'account/manage_account.html')
