from django.shortcuts import render
from django.views import View
import subprocess
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import Person


@login_required
def index(request):
    # Получаем данные из формы
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            first_name = userform.cleaned_data.get("first_name")
            last_name = userform.cleaned_data.get("last_name")
            email = userform.cleaned_data.get("email")
            birthday = userform.cleaned_data.get("birthday")
            year = userform.cleaned_data.get("year")
            person = Person(first_name=first_name, last_name=last_name, email=email, birthday=birthday, year=year)
            person.save()
            return HttpResponseRedirect('/download/')
        else:
            return HttpResponse("Введите корректные данные")
    else:
        userform = UserForm()
    # Вызываем скрипт Python с передачей входных данных из формы в качестве параметров
    #subprocess.run(['python', 'personal_matrix.py', day_of_birth])

    # Возвращаем ответ пользователю
    return render(request, 'new_client/index.html', {'form': userform})

def download(request):
    return render(request, 'new_client/download.html')




#@login_required
#def home(request):
#    if request.method == "POST":
#        userform = UserForm(request.POST)
#        if userform.is_valid():
#            first_name = userform.cleaned_data["first_name"]
 #           last_name = userform.cleaned_data["last_name"]
#            email = userform.cleaned_data["email"]
#            birthday = userform.cleaned_data["birthday"]
#            year = userform.cleaned_data["year"]
 #       else:
 #           return HttpResponse("Введите корректные данные")
#        return HttpResponse(f"<h2>Спасибо, {first_name}! Результаты расчета матрицы и персональные рекомендации отправим на {email}</h2>")
#    else:
#        userform = UserForm()
#    return render(request, "new_client/index.html", {"form": userform})
