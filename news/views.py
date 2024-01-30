from .models import *
from django.shortcuts import render, redirect


# Create your views here.


def asosiy(request):
    projects = Asosiy_pages.objects.all()
    context = {
        'asosiy': projects
    }
    return render(request, "index.html", context)


def noutboklar(request):
    projects = Noutbuklarim.objects.all()
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
    projects = Telefon.objects.all()
    context = {
        'telefon': projects,
    }
    return render(request, "telefon.html", context)
