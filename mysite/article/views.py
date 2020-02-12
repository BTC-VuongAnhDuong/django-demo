# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(Request):
    return HttpResponse('article')

def new(Request):
    return HttpResponse('add new article')