# views are class based.
from django.views.generic import (
    TemplateView, ListView, DetailView, FormView
)

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404

from blog.models import Post, Comment
from blog.forms import CommentForm


class BlogListView(ListView):
    template_name = 'website/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now(), status=True)
        print(self.request.GET)
        if (category :=self.request.GET.get('category')):
            posts = posts.filter(categories__name=category.title())
            # all post categories are in title

        elif (tag :=self.request.GET.get('tag')):
            posts = posts.filter(tags__name=tag.lower())
            # all post tags are lowercase

        elif (given_author :=self.request.GET.get('author')):
            posts = posts.filter(author__username=given_author)

        elif (q := self.request.GET.get('q')):
            posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))
                
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            # If page_number is not an integer, deliver first page.
            page_obj = paginator.page(1)
        except EmptyPage:
            # If page_number is out of range, deliver last page of results.
            page_obj = paginator.page(paginator.num_pages)
        context['posts'] = page_obj
        return context
    

class BlogSingleListView(DetailView, FormView):
    model = Post
    form_class = CommentForm
    context_object_name = 'post'
    template_name = 'blog/blog-single.html'
    slug_url_kwarg = 'pid'
    slug_field = 'pk'

    def get_object(self):
        pid = self.kwargs.get('pid')
        post = get_object_or_404(Post, id=pid, status=True, published_date__lte=timezone.now())
        self.post = post
        return post
    
    def get(self, request, *args, **kwargs):
        reponse = super().get(request, *args, **kwargs)
        # if this post is login_required and user is not logged in
        if request.user.is_authenticated == False and self.post.login_require == True:
            messages.error(request, 'Please Sign in to view VIP Blogs')
            url = reverse('account_login')  + '?next=' + self.object.get_absolute_url()
            return redirect(url)
        
        self.increment_post_view()
        return reponse
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prev_post, next_post = self.find_prev_next_posts()
        comments = self.find_blog_comments()
        context['prev_post'], context['next_post'] = prev_post, next_post
        context['comments'] = comments
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def find_prev_next_posts(self):
        posts = list(Post.objects.filter(published_date__lte=timezone.now(), status=1))
        main_post_index = posts.index(self.post)
        prev_post = None if main_post_index == 0 else posts[main_post_index-1]
        next_post = None if len(posts) == main_post_index + 1 else posts[main_post_index + 1]
        return prev_post, next_post

    def find_blog_comments(self):
        return Comment.objects.filter(post=self.post, approved=True)

    def increment_post_view(self):
        self.post.views += 1
        self.post.save()