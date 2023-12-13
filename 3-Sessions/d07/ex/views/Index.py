from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

class Index(View):
	def get(self, request):
		return HttpResponse("OK :D / DJANGO_SETTINGS_MODULE")