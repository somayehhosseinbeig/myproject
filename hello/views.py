from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def index(request):
    return HttpResponse("Hello, World!")'''

def index(request):
    return render(request, "hello/index.html")

def somayeh(request):
    return HttpResponse("Hello Somayeh")


def arnika(request):
    return HttpResponse("Hello Arnika")

def greet(requset, name):
    return render(requset, "hello/greet.html", {
        "name": name.capitalize()
    })