from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from blog.forms import CommentForm

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
    post = Post.objects.get(id=pid, status=True, published_date__lte=timezone.now())
    context = {}

    # if user is adding a comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            form.instance.username = request.user.username
            form.instance.email = request.user.email

            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment added successfully')
        else:
            print(form.errors)
            messages.add_message(request, messages.ERROR, "your comment didn't added successfully")

    if post:
        form = CommentForm() if request.user.is_authenticated else None
        prev_post, next_post = find_prev_next_posts(post)
        comments = find_blog_comments(post)
        increment_post_view(post)
        context = {'prev_post':prev_post, 'post':post,
                   'next_post':next_post, 'form':form, 'comments':comments}

    return render(request, 'blog-single.html', context)

def find_prev_next_posts(post: Post):
    posts = list(Post.objects.filter(published_date__lte=timezone.now(), status=1))
    main_post_index = posts.index(post)
    prev_post = None if main_post_index == 0 else posts[main_post_index-1]
    next_post = None if len(posts) == 1 else posts[main_post_index + 1]
    return prev_post, next_post


def find_blog_comments(post: Post):
    return Comment.objects.filter(post=post)
    

def increment_post_view(post: Post):
    post.views += 1
    post.save()