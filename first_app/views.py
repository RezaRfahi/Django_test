from django.core.checks.messages import Info
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from Django_test.settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import render,get_object_or_404,reverse
from django.views import generic
from . import models
from django.contrib.auth.forms import UserCreationForm
from django import template
from django.contrib.admin.decorators import register
from django.contrib.auth import login,forms,logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class index(generic.TemplateView):
 
    template_name='first_app/index.html'
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['info_list']=models.Info.objects.order_by("-pub_date")
        context['media_root']=MEDIA_ROOT
        context['media_url']=MEDIA_URL
        return context
        

class info_detail(generic.DetailView):
    template_name='first_app/detail.html'
    model=models.Info

class about(generic.TemplateView):
    template_name='first_app/about.html'
    
class signin(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/signin.html'


class addComment(CreateView):
    model = models.Comment
    template_name = "first_app/detail.html"
