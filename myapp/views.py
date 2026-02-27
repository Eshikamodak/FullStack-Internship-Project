from django.shortcuts import render,redirect
from .models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from .models import User

def register(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not password or not email:
            message = "Please enter all details"

        else:
            existing_user = User.objects.filter(username=username).first()

            if existing_user:
                message = "Username already exists"
            else:
                User.objects.create(
                    username=username,
                    email=email,
                    password=password
                )
                return redirect('addtask')

    return render(request, "register.html", {"message": message})


def addtask(request):
    return render(request, 'addtask.html')
