from django.db import models
from main.models import *
# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render

class Category(models.Model):
    title = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title}'

class Tovar(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=500, blank=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.FloatField(default=0.0, blank=True)
    status = models.IntegerField(default=0, blank=True)
    img1 = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.title} {self.cat.title}'

class Contact(models.Model):
    number = models.CharField(max_length=18, blank=True)
    f_number = models.CharField(max_length=18, blank=True)

    def __str__(self):
        return f'{self.number}'


class Feedback(models.Model):
    name = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    # comment = models.TextField(blank=True,null=True)
    categoriya = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.phone}'


class Service(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    mini_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.title} '

class Partner(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.title} '

class Otziv(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title} '


class Fon(models.Model):
    foto1 = models.ImageField(upload_to='upload', blank=True)
    foto2 = models.ImageField(upload_to='upload', blank=True)
    foto3 = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.foto1}'
