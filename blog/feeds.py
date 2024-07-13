from django.contrib.syndication.views import Feed
from django.core.handlers.wsgi import WSGIRequest
from blog.models import Post, Category
from taggit.models import TaggedItem
from django.urls import reverse
from django.contrib.auth.models import User


class LatestBlogFeed(Feed):
    title = "5 latest blogs"
    link = "/latestblogs/"
    description = "websites 5 latest blogs according to given query"


    def get_object(self, request: WSGIRequest, **kwargs):
        # returns blogs of certain categories & Tags

        if category:= request.GET.get('category'):
            return Category.objects.get(name=category.title())
        
        elif tag:= request.GET.get('tag'):
            return TaggedItem.objects.get(tag_id__name=tag.title())
        
        elif author:= request.GET.get('author'):
            return User.objects.get(username=author)
        
        else:
            return 

    def items(self, obj):

        if type(obj) == Category:
            return Post.objects.filter(categories__name = obj, status=True)[:5]
        
        elif type(obj) == TaggedItem:
            return Post.objects.filter(tags=obj.tag, status=True)[:5]
        
        elif type(obj) == User:
            return Post.objects.filter(author=obj, status=True)[:5]
        
        else:
            return Post.objects.filter(status=True)[:5]

    def item_title(self, item: Post):
        return item.title

    def item_description(self, item: Post):
        return item.content[:50]
    
    def item_pubdate(self, item: Post):
        return item.published_date
    
    def item_updateddate(self, item: Post):
        return item.updated_date
    
    def item_categories(self, item: Post):
        return item.categories.all()
    
    def item_link(self, item: Post):
        return reverse('blog:single' ,kwargs={'pid':item.id})