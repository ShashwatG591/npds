from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

API = "http://127.0.0.1:8000"

def validate(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user  = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            # return HttpResponse("true")
            return redirect(API+'/home/')
        else:
            # return HttpResponse("false")
            messages.error(request, 'Username or Password Incorrect')
            return redirect(API)
    else:
        # return HttpResponse("false")
        messages.error(request, 'Username or Password Incorrect')
        return redirect(API)

def leavepage(request):
    logout(request)
    return redirect(API)

def home(request):
    return render(request,'home.html')