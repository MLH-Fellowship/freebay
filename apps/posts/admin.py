from django.contrib import admin
from apps.posts.models import (
                                Post, 
                                Category
                                )


class CategoryAdmin(admin.ModelAdmin):
   model = Category
   list_display = ['title']


class PostAdmin(admin.ModelAdmin):
   model = Post
   list_display = ['caption']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
