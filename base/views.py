from django.shortcuts import render

def index(request):
    return render(request, 'base/home.html')

def imageSearch(request):
    return render(request, 'base/imageSearch.html')

def dataTracker(request):
    return render(request, 'base/dataTracker.html')