from django.urls import path

from website.views import v1
from website.views import v2

app_name = 'website'

# urlpatterns for views v1
# urlpatterns = [
#     path('contact/', v1.contact_view, name='contact'),
#     path('about/', v1.about_view, name='about'),
# ]

# urlpatterns for views v2
urlpatterns = [
    path('about/', v2.AboutViewTemplateView.as_view(), name='about'),
    path('contact/', v2.ContactViewFormView.as_view(), name='contact')
]
