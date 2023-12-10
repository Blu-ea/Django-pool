from django.urls import path
from . import views

urlpatterns = [
	path('django/', views.django_history),
	path('display/', views.display),
	path('template/', views.template),
]