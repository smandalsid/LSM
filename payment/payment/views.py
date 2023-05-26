from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from barcode.test import *
# Create your views here.

def home(request):
    users=UserProfile.objects.all()
    if request.method=="POST":
        img=request.FILES["img"]
        Images.objects.create(imgid=1, img=img)
        storeimg=Images.objects.get(imgid=1)
        rider=reader("media/"+str(storeimg.img))
        storeimg.delete()
        # print(type(rider))
        user=UserProfile.objects.get(regno=rider)
        user.trips=user.trips+1
        user.balance=user.balance+16
        user.save()

    return render(request, "home.html", locals())