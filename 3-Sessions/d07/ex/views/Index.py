from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

class IndexView(View):
	def get(self, request: HttpRequest):
		
		return render(request, "ex/index.html", {"username": request.user.username})
		return HttpResponse(f"OK :D / DJANGO_SETTINGS_MODULE User {request.user.username}")	