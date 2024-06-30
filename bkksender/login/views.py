from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Login  # Mengimpor model yang benar

root_front = 'login/frontend/'

# Laman Login
def index(request):
    context = {
        'TitlePage': 'Login Panel BKKSender',
        'BrandPage': 'BKKSender',
        'nav': [
            ['/', 'Home'],
            ['/login', 'login'],
        ],
        'css_templates': 'login/frontend/login/snippets/css_templates.html',
        'js_templates': 'login/frontend/login/snippets/js_templates.html',
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            pengguna = Login.empAuth_objects.get(username=username, password=password)

            if pengguna is not None:
                context = {
                    'TitlePage': 'Admin Panel BKKSender',
                    'Heading': 'Admin Panel BKKSender',
                    'nav': [
                        ['/', 'dashboard'],
                        ['/logout', 'profile', 'sender tools'],
                    ],
                    'dashcss_templates': 'dashboard/frontend/dashboard/snippets/css_templates.html',
                    'dashjs_templates': 'dashboard/frontend/dashboard/snippets/js_templates.html',
                }
                return render(request, 'dashboard/frontend/dashboard/index.html', context)
            else:
                print("Seseorang Telah Mencoba Login Namun gagal")
                print("Mereka Menggunakan Username: {} dan password: {}".format(username, password))
                return redirect('dashboard/')
        except Login.DoesNotExist:
            print("Pengguna tidak ditemukan")
            return render(request, f'{root_front}login/index.html', context)
        except Exception as identifier:
            print(f"Error: {identifier}")
            return render(request, f'{root_front}login/index.html', context)
    else:
        return render(request, f'{root_front}login/index.html', context)


def logout(request):
     return HttpResponse("anda keluar ...")

