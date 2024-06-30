from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Home Page untuk app /login/
# template login django import
from django.contrib.auth import login,authenticate
root_front = 'dashboard/frontend/'
# Laman Login
def index(request):

    context = {
        'TitlePage':'Admin Panel BKKSender',
        'Heading':'Admin Panel BKKSender',
         'nav': [
            ['/','dashboard'],
            ['/logout','profile','sender tools'],
            ],
        'dashcss_templates':'dashboard/frontend/dashboard/snippets/css_templates.html',
        'dashjs_templates':'dashboard/frontend/dashboard/snippets/js_templates.html',
        
    }
    return render(request, f'{root_front}dashboard/index.html', context)



