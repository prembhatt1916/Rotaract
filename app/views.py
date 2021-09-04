from django.shortcuts import render
from .models import Hero_Section , Gallery , Notification, Community , International , Club, Vocational, Professional , Council, Director


# Create your views here.


def index(request):
    hero = Hero_Section.objects.all()
    notification = Notification.objects.all()
    
    context={
        'hero' : hero,
        'notification' : notification,
        }
    return render(request, 'index.html', context)



def projects(request):
    notification = Notification.objects.all()
    community = Community.objects.all()
    international = International.objects.all()
    club = Club.objects.all()
    vocational = Vocational.objects.all()
    professional = Professional.objects.all()
    
    context={
        'community' : community,
        'international' : international,
        'club' : club,
        'vocational' : vocational,
        'professional' : professional,
        'notification' : notification,
        }
    return render(request, 'projects.html', context)

def about(request):
    notification = Notification.objects.all()
    context={
        
        'notification' : notification,
        }
    return render(request, 'raccvs.about.html', context)

def rotaryinternational(request):
    notification = Notification.objects.all()
    context={
        
        'notification' : notification,
        }
    return render(request, 'rotaryinternational.html', context)



def gallery(request):
    notification = Notification.objects.all()
    gallery = Gallery.objects.all()
    context={
        'gallery' : gallery,
        'notification' : notification,
        
        }
    return render(request, 'gallery.html', context)

def cvs(request):
    notification = Notification.objects.all()
    context={
        
        'notification' : notification,
        }
    return render(request, 'cvs.html', context)

def rcdsw(request):
    notification = Notification.objects.all()
    context={
        
        'notification' : notification,
        }
    return render(request, 'rcdsw.html', context)

def rotaractdistrict3011(request):
    notification = Notification.objects.all()
    context={
        
        'notification' : notification,
        }
    return render(request, 'rotaractdistrict3011.html', context)

def team(request):
    notification = Notification.objects.all()
    council = Council.objects.all()
    director = Director.objects.all()
    context={
        'council' : council,
        'notification' : notification,
        'director' : director,
        }
    return render(request, 'team.html', context)

def id_card(request):
    notification = Notification.objects.all()
    context={
        
        'notification' : notification,
        }
    return render(request, 'id.card.html', context)

def error_404_view(request , exception):
    return render(request, '404.html')
