from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
# {% url 'blog:category' category=cat %}
def index_view(request,*args, **kwargs):
    posts = Post.objects.filter(status=True)
    print(kwargs)
    print(args)

    # print(request.GET.get('category'))
    if (category :=request.GET.get('category')):
        print(category)
        posts = posts.filter(categories__name=category)

    if (q := request.GET.get('q')):
        print(q)
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
    

def search_view(request):
    posts = Post.objects.filter(status=True)
    posts = get_list_or_404(posts, Q(title__in=keyword) | Q(content__in=keyword))
    context = {'posts':posts}
    return render(request,'index.html', context)


def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')


def increment_post(post: Post):
    post.views += 1
    post.save()