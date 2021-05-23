from django.contrib import admin
from .models import Post, PostRate


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['id', 'post_title', 'post_body', 'rates']
    #prepopulated_fields = {'slug': ('post_title', )}


@admin.register(PostRate)
class AdminPostRate(admin.ModelAdmin):
    list_display = ['likes', 'dislikes']
