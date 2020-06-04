import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import JokeList

def fetchjoke(request, joke="click to add joke"):
    all_obj=list(JokeList.objects.all())
    # print(all_obj[0].content)
    return render(request, 'index.html', {'joke': joke, 'all_obj':all_obj})

def add(request):
    url='http://api.icndb.com/jokes/random'
    j=requests.get(url).json()
    joke=j['value']['joke']
    obj=JokeList(content=joke)
    obj.save()
    all_obj=list(JokeList.objects.all())
    return render(request, 'index.html', {'joke': joke, 'all_obj':all_obj})

def deletejoke(request, jokeid, joke="click to add joke"):
    item=JokeList.objects.get(id=jokeid)
    item.delete()
    all_obj=list(JokeList.objects.all())
    return render(request, 'index.html', {'joke': joke, 'all_obj':all_obj})