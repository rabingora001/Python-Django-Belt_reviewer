from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request, "log_reg/index.html")

def registration_process(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    else:
        hash_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hash_password.decode())
        request.session["user_id"] = new_user.id
        request.session["username"] = new_user.alias
        return redirect("/books")

def login_process(request):
    errors =User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        logged_in_user = User.objects.get(email=request.POST["login_email"])
        request.session["user_id"] = logged_in_user.id
        request.session["username"] = logged_in_user.alias
        return redirect('/books')

def books(request):
    return render(request, 'log_reg/welcome.html')