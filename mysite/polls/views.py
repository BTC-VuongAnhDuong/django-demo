# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Question
from .models import Choice
import datetime

# Create your views here.
def index(request):
    myname = "Vuong Anh duong"
    taisan = ['dien thoai','may tinh','may bay']
    context={
        "name" : myname,
        "items" : taisan
    }
    return render(request,"polls/index.html",context)

def viewList(request):
    list_question = Question.objects.all()
    content = {"list": list_question}
    return render(request, "polls/question_list.html",content)

def questiondetail(request, question_id):
    if(question_id ==False):
        return responseError(request,"Question not found!")
    choices = Choice.objects.filter(question=question_id)
    question = Question.objects.get(id=question_id)
    context = {
        "question": question,
        "choices":choices
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

def questionAdd(request):
    if request.method == "POST":
        question_text = request.POST.get('question_text', False)
        print(question_text)
        if (question_text == False):
            return responseError(request, "Question content is required")
        try:
            question = Question(question_text=question_text,time_pub = datetime.datetime.now())
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
        choice = Choice(choice_text = choice_text,vote=0,question=Question.objects.get(pk=question_id))
        choice.save()
    except Exception as e:
        print(e)
        return HttpResponse("Exception")
    context = {
        "question": Question.objects.get(id=question_id),
        "choices": Choice.objects.filter(question=question_id)
    }
    return render(request, "polls/question_detail.html", context)

def responseError(request,message):
    return render(request,'error.html',{"message":message})