from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def django_history(request):
	return (render(request,"ex01/django.html"))


def display(request):
	return (render(request,"ex01/display.html"))
	

def template(request):
	return (render(request,"ex01/template.html"))
