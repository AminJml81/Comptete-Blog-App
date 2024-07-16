from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index_view(request,*args, **kwargs):
    posts = Post.objects.filter(status=True)

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
    post = Post.objects.filter(id=pid, status=True).first()
    if post:
        increment_post(post)
        context = {'post':post}
        return render(request, 'blog-single.html', context)

def increment_post(post: Post):
    post.views += 1
    post.save()