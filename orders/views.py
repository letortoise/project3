from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from .models import MenuItem


# Create your views here.
def index(request):
    print(request.user)
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    return HttpResponseRedirect(reverse("menu"))

def menu(request):

    # Serialize the menu QuerySet for use with JavaScript
    menuInfo = MenuItem.objects.all()
    menu = serializers.serialize('json', menuInfo)

    # Prepare menu data for templating
    

    context = {
        "menu": menu,
        "menuInfo": menuInfo
    }
    return render(request, "orders/menu.html", context)

def lookup(request):
    try:
        # Get information from XHR
        type = request.POST["type"]
        size = request.POST["size"]
        numExtras = int(request.POST["numExtras"])

        # Lookup menu item
        item = MenuItem.objects.filter(type=type, size=size, numExtras=numExtras).first()
    except KeyError:
        return JsonResponse({"success": False})
    except MenuItem.DoesNotExist:
        return JsonResponse({"success": False})

    return JsonResponse({"success": True, "id": item.pk})

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
