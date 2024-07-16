from allauth.account.views import (password_change,
                                    password_reset, password_reset_done, 
                                    password_reset_from_key, password_reset_from_key_done, 
                                    login, signup, logout)
from django.urls import path, re_path
from account import views

from allauth.account.urls import urlpatterns


urlpatterns = [
    path('manage/', views.manage_account_view , name='manage_account'),

    path("login/", login, name="account_login"),
    path("logout/", logout, name="account_logout"),
    path("signup/", signup, name="account_signup"),

    path('password/change', password_change, name='account_change_password'),

    path('password/reset', password_reset, name='account_reset_password'),
    path('password/reset/done', password_reset_done , name='account_reset_password_done'),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", password_reset_from_key, name='account_reset_password_from_key'),
    path('password/reset/key/done/', password_reset_from_key_done , name='account_reset_password_from_key_done'),
]
