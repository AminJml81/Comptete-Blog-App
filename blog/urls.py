from django.urls import path
from blog import views
from blog.feeds import LatestBlogFeed



app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/<str:category>', views.index_view, name='category'),
    path('tag/<str:tag>', views.index_view, name='tag'),
    path('author/<str:author>', views.index_view, name='author'),
    path('blog/<int:pid>/', views.blog_single_view, name='single'),
    path('404/', views.not_found, name='not_found'),
    #rssfeed
    path("feed/rss/", LatestBlogFeed(), name='rss_feed'),
    path("feed/rss/category/<str:category", LatestBlogFeed(), name='rss_feed_category'),
    path("feed/rss/tag/<str:tag>", LatestBlogFeed(), name='rss_feed_tag'),
    path("feed/rss/author/<str:author>", LatestBlogFeed(), name='rss_feed_author'),
]
