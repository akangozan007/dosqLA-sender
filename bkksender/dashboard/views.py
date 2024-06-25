from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Home Page untuk app /login/
root_front = 'dashboard/frontend/'
# Laman Login
def index(request):
    context = {
        'TitlePage':'Login Panel BKKSender',
    }
    return render(request, f'{root_front}dashboard/index.html', context)


