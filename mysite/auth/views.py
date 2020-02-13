# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import django.contrib import auth
from django.contrib.auth.models import User
import base64
# Create your views here.
def login(request):
    if request.method=='POST':
        userName = request.POST.get('user_name',False)
        password = request.POST.get('password',False)
        myUser = auth.authenticate(username=userName,password=password)
        if userName is None:
            return HttpResponse('Invalid username')
        auth.login(request,myUser)

        redirect = request.POST.get('redirect',False)
        if len(redirect) > 0:
            return return HttpResponseRedirect(base64.b64decode(redirect))
        return render(request,'auth/login.html')
    else:
        data={"redirect":request.GET.get('redirect',False)}
        return render(request,'auth/login.html',data)

def register(request):
    if request.method=='POST':
        userName = request.POST.get('user_name',False)
        password = request.POST.get('password',False)
        email = request.POST.get('email',False)

        if userName is None:
            return HttpResponse('Invalid username')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Duplicate email')
            
        myUser = User.objects.create_user(username=userName,email=email,password=password)

        if not myUser.id:
            return HttpResponse('Invalid data')

        myUser = auth.authenticate(username=userName,password=password)
        
        redirect = request.POST.get('redirect',False)
        if len(redirect) > 0:
            return return HttpResponseRedirect(base64.b64decode(redirect))
        return render(request,'auth/register.html')
    else:
        data={"redirect":request.GET.get('redirect',False)}
        return render(request,'auth/register.html',data)