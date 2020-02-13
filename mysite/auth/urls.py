from django.conf.urls import url
from . import views

urlpatterns = [
    url('login/',views.viewList, name="login" ),
    url('logout/', views.vote,name="logout"),
]

