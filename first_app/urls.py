from first_app import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,static
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import forms,login,logout,views as auth_views


app_name='first_app'

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('about/',views.about.as_view(),name='about'),
    path('<int:pk>/',views.info_detail.as_view(),name='detail'),
    path('<int:pk>/',views.addComment,name='comment'),
    path('accounts/signin',views.signin.as_view(),name='signin'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)