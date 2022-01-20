from django.shortcuts import render

def index(request):
    return render(request, 'base/home.html')

def imageSearch(request):
    return render(request, 'base/imageSearch.html')

def dataTracker(request):
    return render(request, 'base/dataTracker.html')

def AI_Car(request):
    return render(request, 'base/AI_Car.html')

def HMM(request):
    return render(request, 'base/HMM.html')

def Kmeans(request):
    return render(request, 'base/Kmeans.html')

def LinReg(request):
    return render(request, 'base/LinReg.html')