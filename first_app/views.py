from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from Django_test.settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import redirect, render,get_object_or_404,reverse
from django.views import generic
from .models import *
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
        context['info_list']=Info.objects.order_by("-pub_date")
        context['media_root']=MEDIA_ROOT
        context['media_url']=MEDIA_URL
        return context
        

class info_detail(generic.DetailView):
    template_name='first_app/detail.html'
    model=Info

class about(generic.TemplateView):
    template_name='first_app/about.html'
    
class signin(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/signin.html'

def addComment(request, pk):
   info_get=Info.objects.get(id=pk)
   if request.method == 'POST' :
      cm=Comment(info=info_get,commenter_name=request.POST.get('name'),
      comment_dsc=request.POST('description'),
      comment_title=request.POST('cm-title')
      )
   cm.save()
   redirect('/')