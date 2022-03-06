from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def memo(request):
    return HttpResponse("Hello, world. You're at the Memo index.")