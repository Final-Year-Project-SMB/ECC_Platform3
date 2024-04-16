#from django.shortcuts import render
from django.shortcuts import redirect, render


#def index(request):
    #return HttpResponse("Hello, world. You're at the project index.")

def home(request):
    #return HttpResponse('welcome to this page')
    return render(request,"home.html")

def account(request):
    return render(request,"account.html")



# Create your views here.
