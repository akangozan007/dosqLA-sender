from django.http import HttpResponse
import MySQLdb

# Hello World
def index(request):
    return HttpResponse("Hello, world. laman Index BotSender")

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
