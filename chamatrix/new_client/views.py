from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html") 

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    first_name = request.POST.get("first_name", "Undefined")
    last_name = request.POST.get("last_name", "Undefined")
    email = request.POST.get("email", "Undefined")
    birthday = request.POST.get("birthday", "Undefined")
    year = request.POST.get("year", 2023)
    return HttpResponse(f"Спасибо! Мы получили данные. Расчет матрицы с персональными рекомендациями на {year} придет на Вашу почту в течение часа.")

def generate(request):
    return HttpResponse("Генерировать")


