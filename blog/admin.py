from django.contrib import admin
from blog.models import Post, Category 
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    @admin.display(description='short content')
    def short_content(self, obj):
        return obj.content[:40]
    
    date_hierarchy = 'published_date'
    list_display = ('title', 'short_content','views' ,'status', 'published_date','created_date', 'updated_date', 'author')
    #list_display = ('title', 'author', 'views')
    list_filter = ('status', 'categories', 'author')
    # list_filter = ('status', 'author')
    search_fields = ('title', 'auhtor', 'content', 'author')
    
    fieldsets = [
        (
            'Post',
            {
                "fields": ["image", 'author', "title", "content", 'categories'],
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