from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def projects(request):
    return HttpResponse("Here are the products")


def project(request, key):
    return HttpResponse(f"The key is {key}")