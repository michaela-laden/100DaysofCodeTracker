from django.shortcuts import render
from django.http import HttpResponse
from .models import Log

# Create your views here.


def home(request):
    return render(request, 'tracker/home.html')

def tracker(request):
    return render(request, 'tracker/index.html')

def stats(request):
    return render(request, 'tracker/stats.html')

def ideas(request):
    return render(request, 'tracker/ideas.html')

