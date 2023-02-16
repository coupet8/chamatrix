from django.shortcuts import render
from django.views import View
import subprocess
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from new_client import personal_matrix

class IndexView(View):
    template_name = 'new_client/index.html'

    def get(self, request):
        return render(request, self.template_name)
    @login_required
    def post(self, request):
        # Получаем данные из формы
        if request.method == "POST":
            userform = UserForm(request.POST)
            if userform.is_valid():
                first_name = userform.POST.get("first_name")
                last_name = userform.POST.get("last_name")
                email = userform.POST.get("email")
                birthday = userform.POST.get("birthday")
                year = userform.POST.get("year")
            else:
                return HttpResponse("Введите корректные данные")
        # Вызываем скрипт Python с передачей входных данных из формы в качестве параметров
        subprocess.call(['python', 'personal_matrix.py', birthday])

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
