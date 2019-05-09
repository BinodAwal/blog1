from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse("I am home page")
