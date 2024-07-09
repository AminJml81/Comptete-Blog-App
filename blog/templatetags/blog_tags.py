from django import template
from blog.models import Post

register = template.Library()

    
@register.inclusion_tag('blog-categories.html')
def count_blog_categories():
    posts = get_all_posts()
    categories = {}
    for post in posts:
        for cat in post.categories.all():
            if cat in categories:
                categories[cat] += 1
            else:
                categories[cat] = 1
                
    categories = dict(sorted(categories.items(), key=lambda x: x[1], reverse=True))
    return {'categories': categories} 


def get_all_posts():
    posts = Post.objects.filter(status=True)
    return posts
    