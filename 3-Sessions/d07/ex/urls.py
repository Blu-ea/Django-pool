from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="racine"),
    path('register/', views.RegisterView.as_view(), name="register"),
]
