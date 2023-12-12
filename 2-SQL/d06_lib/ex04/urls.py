from django.urls import path
from ex00 import views as views0
from ex02 import views as views2
from . import views

urlpatterns = [
	path('init/', views0.init),
	path('populate/', views2.populate),
	path('display/', views2.display),
	path('remove/', views.remove),
]