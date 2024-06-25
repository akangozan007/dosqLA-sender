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
        ]
    }
    return render(request, f'{root_front}login/index.html', context)


