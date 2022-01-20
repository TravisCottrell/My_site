
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('imageSearch', views.imageSearch, name='imageSearch'),
    path('dataTracker', views.dataTracker, name='dataTracker'),
    path('AI_Car', views.AI_Car, name='AI_Car'),
    path('HMM', views.HMM, name='HMM'),
    path('Kmeans', views.Kmeans, name='Kmeans'),
    path('LinReg', views.LinReg, name='LinReg'),
]