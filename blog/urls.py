from django.urls import path

from blog.views import v1, v2
from blog.feeds import LatestBlogFeed


app_name = 'blog'

# urlpatterns for views v1
# urlpatterns = [
#     path('', v1.index_view, name='index'),
#     path('category/<str:category>', v1.index_view, name='category'),
#     path('tag/<str:tag>', v1.index_view, name='tag'),
#     path('author/<str:author>', v1.index_view, name='author'),
#     path('blog/<int:pid>/', v1.blog_single_view, name='single'),
#     #rssfeed
#     path("feed/rss/", LatestBlogFeed(), name='rss_feed'),
# ]


# urlpatterns for views v1
urlpatterns = [
    path('', v2.BlogListView.as_view(), name='index'),
    path('category/<str:category>', v1.index_view, name='category'),
    path('tag/<str:tag>', v1.index_view, name='tag'),
    path('author/<str:author>', v1.index_view, name='author'),
    path('blog/<int:pid>/', v2.BlogSingleListView.as_view(), name='single'),
    # # rssfeed
    # path("feed/rss/", LatestBlogFeed(), name='rss_feed'),
]
