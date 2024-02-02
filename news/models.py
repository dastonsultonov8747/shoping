from django.db import models


# Create your models here.

class Asosiy_pages(models.Model):
    image = models.ImageField(upload_to='asosiy/', default=None)
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Noutbuklarim(models.Model):
    image = models.ImageField(upload_to='noutbuklarimiz/', default=None)
    brend = models.CharField(max_length=100)
    nomi = models.CharField()
    ekran = models.CharField()
    xotira = models.CharField()
    operativ_xotira = models.CharField()
    operatsion_sistema = models.CharField()
    grafichiskiy = models.CharField()
    rangi = models.CharField()
    narxi = models.CharField()

    def __str__(self):
        return self.nomi


class Kompyuterlar(models.Model):
    image = models.ImageField(upload_to='kompyuterlarimiz/', default=None)
    brend = models.CharField(max_length=100)
    nomi = models.CharField()
    ekran = models.CharField()
    xotira = models.CharField()
    operativ_xotira = models.CharField()
    operatsion_sistema = models.CharField()
    grafichiskiy = models.CharField()
    narxi = models.CharField()

    def __str__(self):
        return self.nomi


class Printer(models.Model):
    image = models.ImageField(upload_to='printerlarimiz/', default=None)
    brend = models.CharField(max_length=100)
    nomi = models.CharField()
    olchami = models.CharField()
    quvati = models.CharField()
    rasm_nisbati = models.CharField()
    narxi = models.CharField()

    def __str__(self):
        return self.nomi


class Oyin_kompyuter(models.Model):
    image = models.ImageField(upload_to='oyin_uchun_komyuterlarimiz/', default=None)
    brend = models.CharField(max_length=100)
    nomi = models.CharField()
    ekran = models.CharField()
    xotira = models.CharField()
    operativ_xotira = models.CharField()
    grafichiskiy = models.CharField()
    operatsion_sistema = models.CharField()
    narxi = models.CharField()

    def __str__(self):
        return self.nomi


class Telefon(models.Model):
    image = models.ImageField(upload_to='telefonlarimiz', default=None)
    brend = models.CharField(max_length=100)
    nomi = models.CharField()
    ekran = models.CharField()
    xotira = models.CharField()
    operativ_xotira = models.CharField()
    narxi = models.CharField()

    def __str__(self):
        return self.nomi


class Ozimiz_haqimizda(models.Model):
    title = models.CharField(max_length=200)
    malumot = models.TextField()

    def __str__(self):
        return self.title
