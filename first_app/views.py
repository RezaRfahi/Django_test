from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

class index(generic.TemplateView):
 
    template_name='first_app/index.html'
    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['info_list']=models.Info.objects.all()
        return context
