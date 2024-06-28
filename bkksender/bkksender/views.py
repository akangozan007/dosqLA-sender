from django.http import HttpResponse
# import tags template render
from django.shortcuts import render
root_front = 'bkksender/frontend/'
import MySQLdb


# Hello World
def index(request):
    # template tags
    context = {
        'Heading':'Hello, world. laman Index BotSender',
        'judulSitus':'Selamat Datang Di BKK Sender',
        'BrandPage':'BKKSender',
         'nav': [
            ['/','Home'],
            ['/login','login']
        ],
        'bkksendercss_templates' : 'bkksender/frontend/bkksender/snippets/css.html',
        'bkksenderjs_templates' : 'bkksender/frontend/bkksender/snippets/js.html',
    }
    # ./template tags
    return render(request, f"{root_front}bkksender/index.html", context)

def login(request):
    return HttpResponse("Hello, world. laman login BotSender")

def cekdb(request):
    try:
        db = MySQLdb.connect(
            host="10.11.12.3",
            user="root",
            passwd="12345678",
            db="bkksender"
        )
        # print("Koneksi berhasil!")
        return HttpResponse("Berhasil Connect")
        db.close()
    except MySQLdb.OperationalError as e:
       return HttpResponse("Gagal Connect")
