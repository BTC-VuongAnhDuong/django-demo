# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
import urllib
# Create your views here.
def login(request):
    if request.method=='POST':
        userName = request.POST.get('user_name',False)
        password = request.POST.get('password',False)
        myUser = auth.authenticate(username=userName,password=password)
        data = {}
        if myUser is None:
            data = { "error": 'Invalid username or password','userName':userName }
            # setattr(data,'error','Invalid username or password')
            # data.error = 'Invalid username or password'
            return render(request,'appuser/login.html',data)

        auth.login(request,myUser)

        redirect = request.POST.get('redirect')
        if redirect:
            redirect = urllib.unquote(redirect)
            return HttpResponseRedirect(redirect)
        return HttpResponseRedirect('/')
    else:
        redirect = request.GET.get('next')
        data = {"error":False}
        if redirect:
            data = {"error": False,'redirect':redirect}
        return render(request,'appuser/login.html',data)

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
        if redirect:
            return HttpResponseRedirect(urllib.unquote(redirect))
        return HttpResponseRedirect('/')
    else:
        redirect = request.GET.get('redirect')
        data = {}
        if redirect:
            data.redirect = urllib.unquote(redirect)
        return render(request,'appuser/register.html',data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/auth/login')