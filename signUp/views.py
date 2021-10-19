from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(req):
    return render(req, 'index.html')


def reg(req):
    if req.method == "POST":
        name = req.POST.get('name')
        isauth=req.POST.get('isauth')
        email = req.POST.get('email')
        cno = req.POST.get('phone')
        pwd1 = req.POST.get('password')
        pwd2 = req.POST.get('password-repeat')
        print(pwd1, pwd2)
        user = User.objects.create_user(username=isauth, email=email, password=pwd1, first_name=name,last_name=cno)
        user.save()
        messages.success(req, "error")
    return redirect(to='signUp')
