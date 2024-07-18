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


@register.inclusion_tag('blog-trendingposts.html')
def trending_posts():
    posts = Post.objects.all().order_by('-views')[:3]
    return {'post1':posts[0], 'posts':posts[1:]}


def get_all_posts():
    posts = Post.objects.filter(status=True)
    return posts
