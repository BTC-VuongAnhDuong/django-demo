# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length = 200)
    time_pub = models.DateTimeField()
    user_label = models.CharField(max_length = 200,default='')
    user_id = models.IntegerField(default = 0)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 100)
    vote = models.IntegerField(default=0)
    user_label = models.CharField(max_length = 200,default='')
    user_id = models.IntegerField(default = 0)
    def __str__(self):
        return self.question.question_text+" > "+self.choice_text