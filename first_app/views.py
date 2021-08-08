from Django_test.settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

class index(generic.TemplateView):
 
    template_name='first_app/index.html'
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['info_list']=models.Info.objects.all()
        context['media_root']=MEDIA_ROOT
        context['media_url']=MEDIA_URL
        return context

class info_detail(generic.DetailView):
    template_name='first_app/detail.html'
    model=models.Info

class about(generic.TemplateView):
    template_name='first_app/about.html'