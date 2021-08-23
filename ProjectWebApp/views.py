from django.shortcuts import render, HttpResponse
from services.models import Service

# Create your views here.

def home(request):
    return render(request, "ProjectWebApp/home.html")

def services(request):
    services = Service.objects.all()
    return render(request, "ProjectWebApp/services.html", {"services": services})

def shop(request):
    return render(request, "ProjectWebApp/shop.html")

def blog(request):
    return render(request, "ProjectWebApp/blog.html")    

def contact(request):
    return render(request, "ProjectWebApp/contact.html")  