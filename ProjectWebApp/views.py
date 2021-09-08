from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ProjectWebApp/home.html")

def shop(request):
    return render(request, "ProjectWebApp/shop.html")



