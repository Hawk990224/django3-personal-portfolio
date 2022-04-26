from django.shortcuts import render
from django.http import HttpResponse

from portfolio.models import Project
#from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def about(request):
    return render(request, 'portfolio/about.html')
