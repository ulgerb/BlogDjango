from django.contrib import admin
from myApp.models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    # list_display_links = ['publishing_date']
    # list_filter = ['publishing_date']
    search_fields = ['name', 'textpost']    
    
    class Meta:
        model = Post
        
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = (
        "pk",
        "title",
        "slug",
    )
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

