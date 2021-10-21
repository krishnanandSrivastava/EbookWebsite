from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(req):
    return render(req, 'signup.html')


def reg(req):
    if req.method == "POST":
        name = req.POST.get('name')
        isauth=req.POST.get('isauth')
        if isauth:
            isauth="yes"
        else:
            isauth="no"
        email = req.POST.get('email')
        cno = req.POST.get('phone')
        pwd1 = req.POST.get('password')
        pwd2 = req.POST.get('password-repeat')
        print(isauth)
        user=False
        try:
            user = User.objects.create_user(username=email, email=name, password=pwd1, first_name=isauth,last_name=cno)
            user.save()
        except Exception as e:
            messages.error(req, e)
        if user:
            messages.success(req, "Signup Successful")
    return redirect(to='signUp')
