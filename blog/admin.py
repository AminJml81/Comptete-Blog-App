from django.contrib import admin
from blog.models import Post, Category, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    @admin.display
    def short_content(self, obj):
        return obj.content[:40]
    
    date_hierarchy = 'published_date'
    list_display = ('title', 'short_content','views' ,'login_require','status', 'published_date','created_date', 'updated_date', 'author')
    list_filter = ('status', 'login_require', 'categories', 'author',)
    search_fields = ('title', 'auhtor', 'content', 'author')
    
    fieldsets = [
        (
            'Post',
            {
                "fields": ["image", 'author', "title", "content", 'login_require'],
            },
        ),
        (
            "Grouping Options",
            {
                "classes": ["wide"],
                "fields": ['categories', 'tags'],
            },
        ),
        (
            "Publishing Options",
            {
                "classes": ["wide"],
                "fields": ["status", "published_date"],
            },
        ),
        (
            "Extra Detail",
            {
                "classes": ["collapse"],
                "fields": ["views", "time_to_read"],
            },
        ),
    ]
    

@admin.register(Category)    
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('username', 'email', 'post', 'approved', 'message')
    list_filter = ('username', 'post', 'approved',)
    search_fields = ('username', 'post', 'message')

