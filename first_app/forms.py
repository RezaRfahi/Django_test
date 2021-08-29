from django import forms
from django.db.models.base import Model
from django.forms import fields
from . import models

class AddComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields=('commenter_name',
        'comment_dsc',
        'comment_title')