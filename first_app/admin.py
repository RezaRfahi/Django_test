from django.contrib import admin
from . import models
from django.contrib.admin.decorators import display, register
from typing import Text


class AuthorInline(admin.TabularInline):
    '''Tabular Inline View for '''
    model = models.Info
    extra = 1

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','family']
    inlines=[AuthorInline]

@admin.register(models.Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=['title']
    

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['commenter_name','comment_title']
