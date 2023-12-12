from django.urls import path
from ex00 import views as views0
from . import views

urlpatterns = [
	path('init/', views0.init),
	path('populate/', views.populate),
	path('display/', views.display),
]