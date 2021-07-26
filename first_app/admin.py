from django.contrib import admin
from . import models
from django.contrib.admin.decorators import display, register
from typing import Text

# Register your models here.

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','family']

@admin.register(models.Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=['title']
