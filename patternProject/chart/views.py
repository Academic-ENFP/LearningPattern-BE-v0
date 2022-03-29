from django.shortcuts import render
from django.http import HttpResponse


def chart(request):
    return HttpResponse("Hello, world. You're at the Chart index.")