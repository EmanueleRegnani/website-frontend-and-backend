from django.shortcuts import render
from .models import Article, Event, Gallery_Picture

def main(request):
    arts = Article.objects.all()
    evs = Event.objects.all()
    pics = Gallery_Picture.objects.all()
    context = {
        'articles': arts,
        'events': evs,
        'pictures': pics
    }
    return render(request, 'articles/main.html', context)

def services(request):
    arts = Article.objects.all()
    evs = Event.objects.all()
    pics = Gallery_Picture.objects.all()
    context = {
        'articles': arts,
        'events': evs,
        'pictures': pics
    }
    return render(request, 'articles/services.html', context)

def about(request):
    arts = Article.objects.all()
    evs = Event.objects.all()
    pics = Gallery_Picture.objects.all()
    context = {
        'articles': arts,
        'events': evs,
        'pictures': pics
    }
    return render(request, 'articles/about.html', context)