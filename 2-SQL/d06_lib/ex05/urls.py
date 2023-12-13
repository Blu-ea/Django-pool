from django.urls import path
from . import views
from ex03 import views as views3

urlpatterns = [
	path('populate/', views.populate),
	path('display/', views.display),
	path('remove/', views.remove.as_view())
]