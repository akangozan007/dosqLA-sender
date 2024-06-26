"""bkksender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from . import views
from login import views as Views_Login
from django.conf.urls import url, include
from django.urls import path
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world. laman Index BotSender")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    url(r'^$', views.index, name='index'),
    # url(r'^login/$', include(about.urls)),
    # url(r'^login/$', Views_Login.index, name='index'),
    # path('login', include('login.urls')),
    url(r'^login/$', include('login.urls')),
    url(r'^logout/$', include('login.urls')),
    url(r'^dashboard/$', include('dashboard.urls')),
    url(r'^koneksi/$', views.cekdb, name='cekdb')
]
