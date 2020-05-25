from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_time', 'url']
    fields = ['name', 'email', 'text', 'post', 'url']


admin.register(Comment, CommentsAdmin)