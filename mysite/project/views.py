#from django.shortcuts import render
from django.shortcuts import redirect, render


#def index(request):
    #return HttpResponse("Hello, world. You're at the project index.")

def index(request):
    #return HttpResponse('welcome to this page')
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def account(request):
    return render(request,"account.html")

def about(request):
    return render(request,"about.html")

def engineer(request):
    return render(request,"engineer.html")


def register(request):
    return render(request,"registration.html")

def login(request):
    return render(request,"login.html")

# Create your views here.
