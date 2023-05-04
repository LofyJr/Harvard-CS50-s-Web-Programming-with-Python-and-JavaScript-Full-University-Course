from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def Lofy(request):
    return HttpResponse("Hello, Lofy!")

def Junior(request):
    return HttpResponse("Hello, Junior!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })