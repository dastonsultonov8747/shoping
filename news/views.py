from .models import *
from django.shortcuts import render, redirect
import requests


# Create your views here.


def asosiy(request):
    projects = Asosiy_pages.objects.all()
    context = {
        'asosiy': projects
    }
    return render(request, "index.html", context)


def noutboklar(request):
    projects = requests.get('https://sheetdb.io/api/v1/9hxiqor7ngy49').json()
    context = {
        'noutbuk': projects,
    }
    return render(request, "noutboklarim.html", context)


def kompyuterlar(request):
    projects = Kompyuterlar.objects.all()
    context = {
        'kompyuter': projects,
    }
    return render(request, "kompyuterlar.html", context)


def oyin_uchun_kompyuter(request):
    projects = Oyin_kompyuter.objects.all()
    context = {
        'oyin_kompyuter': projects,
    }
    return render(request, "oyin_kompyuter.html", context)


def printer(request):
    projects = Printer.objects.all()
    context = {
        'printer': projects,
    }
    return render(request, "printer.html", context)


def telefon(request):
    projects = requests.get('https://sheetdb.io/api/v1/9hxiqor7ngy49').json()
    context = {
        'telefon': projects,
    }
    return render(request, "mahsulot.html", context)
