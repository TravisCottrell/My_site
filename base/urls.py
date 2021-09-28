
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('imageSearch', views.imageSearch, name='imageSearch'),
    path('dataTracker', views.dataTracker, name='dataTracker'),
]