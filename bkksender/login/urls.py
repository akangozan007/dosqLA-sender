from django.conf.urls import url
from django.urls import path
from . import views
# import views punyanya login
# bikin url untuk app about
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    # url /keahlian/ subfolder app login
    # url(r'^keahlian/$', views.skills), 
]