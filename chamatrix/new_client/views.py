from django.shortcuts import render
from django.views import View
import subprocess
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm


@login_required
def index(self, request):
    generatebutton = request.POST.get("generate")
    firstname = ''
    lastname = ''
    emailvalue = ''
    day_of_birth = ''
    yearvalue = ''

    # Получаем данные из формы
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            firstname = userform.cleaned_data.get("first_name")
            lastname = userform.cleaned_data.get("last_name")
            emailvalue = userform.cleaned_data.get("email")
            day_of_birth = userform.cleaned_data.get("birthday")
            yearvalue = userform.cleaned_data.get("year")
        else:
            return HttpResponse("Введите корректные данные")
    # Вызываем скрипт Python с передачей входных данных из формы в качестве параметров
    subprocess.run(['python', 'personal_matrix.py', day_of_birth])

    # Возвращаем ответ пользователю
    return render(request, self.template_name, {'message': 'Расчет выполнен!'})




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
