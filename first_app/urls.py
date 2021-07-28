from first_app import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,static
from django.conf import settings
from . import views



app_name='first_app'

urlpatterns = [
    url(r'^$',views.index.as_view(),name='index'),
    url(r'^(?P<pk>\w+)/$',views.info_detail.as_view(),name='detail')
    
]