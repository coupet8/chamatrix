from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def send(request):
    return HttpResponse("Отправить")

def generate(request):
    return HttpResponse("Генерировать")
