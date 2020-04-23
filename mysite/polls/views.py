# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Choice
from .models import Question
from django.contrib.auth import decorators
from django.forms.models import model_to_dict
import json

def index(request):
    myname = "Vuong Anh duong"
    taisan = ['dien thoai','may tinh','may bay']
    context={
        "name" : myname,
        "items" : taisan
    }
    return render(request,"polls/app/dist/index.html",context)

def viewList(request):
    list_question = Question.objects.all().values()
    context = {
        "data": list(list_question),
        "meta": {},
        'pagination': []
    }
    return JsonResponse(context)

def questiondetail(request, question_id):
    if(question_id ==False):
        return responseError(request,"Question not found!")
    choices = Choice.objects.filter(question=question_id)
    question = Question.objects.get(id=question_id)
    context = {
        "question": question,
        "choices":choices,
        'starRange': range(1,6)
    }
    return render(request, "polls/question_detail.html",context)

def vote(request):
    question_id = request.POST.get('question_id',False)
    answer = request.POST.get('answer',False)
    if(answer==False):
        return responseError(request,"Please submit your answer")
    try:
        choice = Choice.objects.get(pk=answer)
        choice.vote +=1
        choice.save()
    except:
        HttpResponse("Exception")
    context = {
        "question": Question.objects.get(id=question_id),
        "choices": Choice.objects.filter(question=question_id)
    }
    return render(request, "polls/question_detail.html",context)

@decorators.login_required(login_url='/auth/login/')
def questionAdd(request):
    if request.method == "POST":
        question_text = request.POST.get('question_text', False)
        print(question_text)
        if (question_text == False):
            return responseError(request, "Question content is required")
        try:
            question = Question(question_text=question_text,time_pub = datetime.datetime.now())
            if request.user.id:
                question.user_id = request.user.id
                question.user_label = request.user.username
            else:
                question.user_label = request.POST.get('username')
            question.save()
        except Exception as e:
            print(e)
            return HttpResponse("Exception")
        return HttpResponseRedirect("/question/detail/"+str(question.id))
    else:
        return render(request, "polls/question_add.html")


def addAnswer(request):
    question_id = request.POST.get('question_id', False)
    choice_text = request.POST.get('choice_text', False)
    if (question_id == False):
        return responseError(request, "Invalid question")
    if (choice_text == False):
        return responseError(request, "Please submit your answer")
    try:
        choice = Choice(choice_text = choice_text,vote=request.POST.get('vote',1),question=Question.objects.get(pk=question_id))
        if request.user.id:
            choice.user_id = request.user.id
            choice.user_label = request.user.username
        else:
            choice.user_label = request.POST.get('username')
        choice.save()
    except Exception as e:
        print(e)
        return HttpResponse("Exception")
    return HttpResponseRedirect("/question/detail/"+str(question_id))

def responseError(request,message):
    return render(request,'error.html',{"message":message})
