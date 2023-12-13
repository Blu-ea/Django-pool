from django.urls import path
from . import views
from ex02 import views as views2
from ex04 import views as views4

urlpatterns = [
	path('init/', views.init),
	path('populate/', views2.populate),
	path('display/', views2.display),
	path('update/', views.update.as_view())
]