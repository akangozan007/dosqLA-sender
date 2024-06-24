from django.conf.urls import url 
# import views punyanya login
# bikin url untuk app about
urlpatterns = [
    url(r'^$', views.index),
    # url /keahlian/ subfolder app login
    # url(r'^keahlian/$', views.skills), 
]