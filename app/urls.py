from django.contrib import admin
from django.urls import path , include
from app import views


urlpatterns = [
    path("",views.index,name="index"),
    path('projects', views.projects, name="projects"),
    path('about', views.about, name="about"),
    path('rotaryinternational', views.rotaryinternational, name="rotaryinternational"),
    path('gallery', views.gallery, name="gallery"),
    path('cvs', views.cvs, name="cvs"),
    path('rcdsw', views.rcdsw, name="rcdsw"),
    path('rotaractdistrict3011', views.rotaractdistrict3011, name="rotaractdistrict3011"),
    path('team', views.team, name="team"),
    path('id_card', views.id_card, name="id_card"),
    
]