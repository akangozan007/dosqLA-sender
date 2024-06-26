from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Home Page untuk app /login/
root_front = 'dashboard/frontend/'
# Laman Login
def index(request):
    context = {
        'TitlePage':'Admin Panel BKKSender',
        'Heading':'Admin Panel BKKSender',
         'nav': [
            ['/','dashboard'],
            ['/logout','profile','sender tools'],
        ]
    }
    return render(request, f'{root_front}dashboard/index.html', context)


