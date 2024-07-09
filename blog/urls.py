from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/<str:category>', views.index_view, name='category'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('search/<str:keyword>', views.search_view, name='search'),
    path('blog/<int:pid>/', views.blog_single_view, name='single'),
]
