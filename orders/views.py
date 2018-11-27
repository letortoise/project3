from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import MenuItem


# Create your views here.
def index(request):
    print("index view is running")
    print(request.user.is_authenticated)
    print(request.user)
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, "orders/login.html", {"message": None})
    return HttpResponseRedirect(reverse("menu"))

def menu(request):

    context = {
        "menu": MenuItem.objects.all()
    }
    return render(request, "orders/menu.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is None:
        return render(request, "order/login.html", {"message": "Something went wrong"})
    else:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
