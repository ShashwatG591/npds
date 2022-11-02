from urllib import request
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

def mainpage(request):
    user = User.objects.all()
    return render(request, 'main.html',{user:'user'})

def adminmain(request):
    return render(request, 'admin-main.html')

def usermain(request):
    user = User.objects.all()
    return render(request, 'user-main.html',{user:'user'})

def admin_profile(request):
    return render(request, 'admin-profile.html')

def checkRecords(request):
    return render(request, 'check-records.html')  

def addAuthority(request):
    return render(request, 'add-authority.html')

def checkAuthority(request):
    return render(request, 'check-authority.html')

def addUser(request):
    return render(request, 'add-user.html')

def viewUser(request):
    return render(request, 'view-user.html')

def deleteUser(request):
    return render(request, 'delete-user.html')

def change_password(request):
    return render(request, 'change-password.html')

def passChange(request):
    user  = User.objects.get(pk=request.POST['uid'])
    if 'password2' in request.POST:
        password = request.POST['password2']
    else:
        password = ""
    
    username = request.POST['username']

    if password!="":
        user.set_password(password)
        user.save()
        # userAuth(request,username,password)
        messages.success(request, 'Password changed Successfully !!')
        return redirect(API)
    else:
        messages.error(request, 'Something went Wrong !!')
        return redirect(API+"change-password")

def userAuth(request,username,password):
    result = checkUser(username)
    user  = authenticate(username=username,password=password)
        
    if user is not None:
        if result == 1:
            login(request,user)

API = "http://127.0.0.1:8000"

def validate(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        result = checkUser(username)
        user  = authenticate(username=username,password=password)
        print(user,result)
        if user is not None:
            if result == 1:
                login(request,user)
                # return HttpResponse("true")
                return redirect(API+'/admin-main/')
            else:
                login(request,user)
                # return HttpResponse("true")
                return redirect(API+'/user-main/')
        else:
            # return HttpResponse("false")
            messages.error(request, 'Username or Password Incorrect')
            return redirect(API)
    else:
        # return HttpResponse("false")
        messages.error(request, 'Username or Password Incorrect')
        return redirect(API)

def checkUser(username):
    query = "SELECT is_superuser FROM auth_user WHERE username='" + username + "';"
    with connection.cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchone()
        result = res[0]
    return result 

def leavepage(request):
    logout(request)
    return redirect(API)

