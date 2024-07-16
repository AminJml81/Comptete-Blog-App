from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index_view(request,*args, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=True)

    if (category :=request.GET.get('category')):
        posts = posts.filter(categories__name=category.title())

    elif (tag :=request.GET.get('tag')):
        posts = posts.filter(tags__name=tag.title())

    elif (given_author :=request.GET.get('author')):
        posts = posts.filter(author__username=given_author)

    elif (q := request.GET.get('q')):
        posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))

    
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {'posts':posts}
    return render(request, 'index.html', context)

def blog_single_view(request, pid:int):
    post = Post.objects.filter(id=pid, status=True, published_date__lte=timezone.now()).first()
    context = {}
    if post:
        prev_post, next_post = find_prev_next_posts(post)
        increment_post_view(post)
        context = {'prev_post':prev_post, 'post':post, 'next_post':next_post}

    return render(request, 'blog-single.html', context)

def find_prev_next_posts(post: Post):
    posts = list(Post.objects.filter(published_date__lte=timezone.now(), status=1))
    main_post_index = posts.index(post)
    prev_post = None if main_post_index == 0 else posts[main_post_index-1]
    next_post = None if len(posts) == 1 else posts[main_post_index + 1]
    print(next_post)
    return prev_post, next_post

def increment_post_view(post: Post):
    post.views += 1
    post.save()