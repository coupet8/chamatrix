from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from new_client import personal_matrix

def download(request):
    return render(request, "new_client/index.html")

@login_required
def home(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            first_name = userform.cleaned_data["first_name"]
            last_name = userform.cleaned_data["last_name"]
            email = userform.cleaned_data["email"]
            birthday = userform.cleaned_data["birthday"]
            year = userform.cleaned_data["year"]
        else:
            return HttpResponse("Введите корректные данные")
#        return HttpResponse(f"<h2>Спасибо, {first_name}! Результаты расчета матрицы и персональные рекомендации отправим на {email}</h2>")
    else:
        userform = UserForm()
<<<<<<< HEAD
        return render(request, "new_client/index.html", {"form": userform})
=======
    return render(request, "new_client/index.html", {"form": userform})
>>>>>>> d524391e00205e85ff5da892ef7627dfb722aefa
