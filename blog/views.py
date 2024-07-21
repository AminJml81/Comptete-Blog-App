from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from blog.forms import CommentForm


# Create your views here.
def index_view(request, *args, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=True)
    if (category :=kwargs.get('category')):
        posts = posts.filter(categories__name=category.title())
        # all post categories are title


    elif (tag :=kwargs.get('tag')):
        posts = posts.filter(tags__name=tag.lower())
        # all post tags are lowercase

    elif (given_author :=kwargs.get('author')):
        posts = posts.filter(author__username=given_author)

    elif (q := request.GET.get('q')):
        posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))

    
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {'posts':posts}
    return render(request, 'website/index.html', context)



def blog_single_view(request, pid:int):
    post = Post.objects.get(id=pid, status=True, published_date__lte=timezone.now())
    context = {}
    # if user is adding a comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        blog_single_post_view(request, form, post)

    # if this post is login_required and user is not logged in
    if request.user.is_authenticated == False and post.login_require == True:
        messages.error(request, 'Please Sign in to view VIP Blogs')
        url = reverse('account_login')  + '?next=' + post.get_absolute_url()
        return redirect(url)
    
    if post:
        form = CommentForm() if request.user.is_authenticated else None
        prev_post, next_post = find_prev_next_posts(post)
        comments = find_blog_comments(post)
        increment_post_view(post)
        context = {'prev_post':prev_post, 'post':post,
                   'next_post':next_post, 'form':form, 'comments':comments}

    return render(request, 'blog/blog-single.html', context)


def blog_single_post_view(request, form, post):
    # Post Method for blog single, (User is adding a comment)
    COMMENT_SUCCESS_MESSAGE = 'your comment added successfully'
    COMMENT_FAILURE_MESSAGE = "your comment didn't added successfully"
    if form.is_valid():
        form.instance.post = post
        form.instance.username = request.user.username
        form.instance.email = request.user.email

        form.save()
        messages.success(request, COMMENT_SUCCESS_MESSAGE)

    else:

        messages.error(request, COMMENT_FAILURE_MESSAGE)

    
def find_prev_next_posts(post: Post):
    posts = list(Post.objects.filter(published_date__lte=timezone.now(), status=1))
    main_post_index = posts.index(post)
    prev_post = None if main_post_index == 0 else posts[main_post_index-1]
    next_post = None if len(posts) == main_post_index + 1 else posts[main_post_index + 1]
    return prev_post, next_post


def find_blog_comments(post: Post):
    return Comment.objects.filter(post=post, approved=True)

def increment_post_view(post: Post):
    post.views += 1
    post.save()


def not_found(request):
    return render(request,'404.html')