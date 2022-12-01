from urllib import request
from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
from subprocess import run, PIPE
import sys
import cv2
from PIL import Image
from pytesseract import pytesseract

API = "http://127.0.0.1:8000/"

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def viewUser(request):
    all_entries = User.objects.all()
    print(all_entries)
    return render(request, 'view-users.html',{ 'all_entries' :all_entries})

def deleteUser(request):
    all_data = User.objects.all()
    return render(request, 'delete-user.html',{'all_data':all_data})

def mainpage(request):
    user = User.objects.all()
    return render(request, 'main.html',{'user':user})

def adminmain(request):
    return render(request, 'admin-main.html')

def usermain(request):
    user = User.objects.all()
    return render(request, 'user-main.html',{'user':user})

def usermainpage(request):
    return render(request, 'user-main-page.html')

def admin_profile(request):
    return render(request, 'admin-profile.html')

def user_profile(request):
    return render(request, 'user-profile.html')

def checkRecords(request):
    all_entries = numPlateRecords.objects.all()
    return render(request, 'check-records.html', {'all_entries':all_entries})  

def check_records_user(request):
    all_entries = numPlateRecords.objects.all()
    return render(request, 'check-records-user.html', {'all_entries':all_entries})

def addAuthority(request):
    return render(request, 'add-authority.html')

def checkAuthority(request):
    all_entries = authorities.objects.all()
    print(all_entries)
    return render(request, 'check-authority.html',{'all_entries':all_entries})

def addUser(request):
    return render(request, 'add-user.html')

def addusertodb(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if firstname!='' and lastname!=''and email!='' and username!='' and password!='':
            if firstname!='' and lastname!=''and email!='' and username!='':
                normalUser = NormalUser(first_name=firstname, last_name=lastname,email=email,username=username)
                normalUser.save()
            addUser = User.objects.create_user(first_name=firstname, last_name=lastname,email=email,username=username, password=password)
            addUser.save()
            messages.success(request, 'User Added Successfully !!')
            return redirect(API+'add-user')
        else:
            messages.error(request, 'Something Went Wrong !!')
            return redirect(API+'add-user')

def addAuth(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        contactNo = request.POST['contact']
        location = request.POST['location']

        if name!='' and email!=''and contactNo!='' and location!='':           
            addAuth = authorities(name=name, contact=contactNo,location=location,email=email)
            addAuth.save()
            # return HttpResponse("done")
            messages.success(request, 'Authority Added Successfully !!')
            return redirect(API+'add-authority')
        else:
            # return HttpResponse("not done")
            messages.error(request, 'Something Went Wrong !!')
            return redirect(API+'add-authority')

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
        logout(request)
        return redirect(API)
    else:
        messages.error(request, 'Something went Wrong !!')
        return redirect(API+"change-password")

def change_pass_user(request):
    return render(request, 'change-pass-user.html')

def changePass(request):
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
        logout(request)
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
                return redirect(API+'admin-main/')
            else:
                login(request,user)
                # return HttpResponse("true")
                return redirect(API+'user-main-page/')
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


def camerarequest(request):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)

    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray,(28,28))
                print("Resized...")
                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")
            
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    auth,num = tesseract()
    if auth ==1:
        AddtoDB(num,auth)
        messages.success(request, 'Number Plate Authenticated')
        return redirect(API+"user-main-page")
    else:
        AddtoDB(num,'0')
        messages.error(request, 'Unauthorised Numberplate')
        return redirect(API+"user-main-page")

def tesseract():
    path_to_tesseract = r'C:\Users\HP\AppData\Local\Tesseract-OCR\tesseract.exe'
    imagepath = 'saved_img.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(imagepath))
    print(text[:])
    result = checkNP(text[:])
    return result,text[:]


def checkNP(num):
    if num !="":
        query1 = "SELECT `auth` FROM `npdetection_numberplate` WHERE `numberPlate` ="+num+";"
        with connection.cursor() as cursor:
            cursor.execute(query1)
            res = cursor.fetchone()
            result = res[0]
        return result

def AddtoDB(num,auth):
    res = numPlateRecords(numplate=num,auth=auth)
    res.save()
# C:\Users\Rahul\AppData\Local\Tesseract-OCR\tesseract.exe