from django.shortcuts import render
from django.http import HttpResponse
from . import models

example = """
    name : text halo,
    date : date YYYY-MM-DD | DD.MM.YYYY 2024-10-12,
    phone : phone +79999999999,
    email : email example@yandex.ru
"""

def index(request):
    return HttpResponse("Добро пожаловать на главную страницу.")


def loadInfo(request):
    phone = request.GET.get("phone", "Undefined")
    name = request.GET.get("name", "Undefined")
    email = request.GET.get("email", "Undefined")
    date = request.GET.get("date", "Undefined")

    if "Undefined" in [phone, name, email, date]:
        return HttpResponse(example)
    
    if models.validPhone(phone) and models.valiDate(date) \
        and models.validEmail(email):
        return HttpResponse(models.searchQuery(name, date, phone, email))
            
    return HttpResponse(example)
