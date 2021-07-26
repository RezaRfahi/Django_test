from first_app import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index.as_view(),name='index')
]