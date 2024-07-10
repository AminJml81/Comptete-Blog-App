from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/<str:category>', views.index_view, name='category'),
    path('blog/<int:pid>/', views.blog_single_view, name='single'),
]
