from django.conf.urls import url
from . import views

urlpatterns = [
    url('detail/(?P<question_id>[0-9]+)', views.questiondetail, name="questionDetail"),
    url('list/',views.viewList, name="questionList" ),
    url('vote/', views.vote,name="vote"),
    url('add/', views.questionAdd, name="questionAdd"),
    url('addAnswer/', views.addAnswer, name="addAnswer"),
    url('',views.index ),
]

