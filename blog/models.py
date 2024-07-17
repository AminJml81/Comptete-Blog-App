from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self) -> str:
        return self.name
    

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    title = models.CharField(max_length=255, null=False, blank=False ) 
    content = models.TextField(max_length=1024, null=False, blank=False )
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    published_date =models.DateTimeField(null=False, blank=False)
    status = models.BooleanField(default=1)
    views = models.PositiveIntegerField(default=0)
    time_to_read = models.PositiveIntegerField(default=1)
    
    class meta:
        ordering = ('-created_date',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.pk})
        
        
class Comment(models.Model):
    message = models.TextField(max_length=1024, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_date']
        
    def __str__(self) -> str:
        return self.message[:20]