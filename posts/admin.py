"""Post Admin Classes"""
# Django 
from django.contrib import admin

# Models
from posts.models import Posts

# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    pass