from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Home Page untuk app /login/
root_front = 'login/frontend/'
# Laman Login
def index(request):
    context = {
        'TitlePage':'Login Panel BKKSender',
        'BrandPage':'BKKSender',
        'nav': [
            ['/','Home'],
            ['/login','login']
        ],
        'css_templates' : 'login/frontend/login/snippets/css_templates.html',
        'js_templates' : 'login/frontend/login/snippets/css_templates.html',

    }
    return render(request, f'{root_front}login/index.html', context)


