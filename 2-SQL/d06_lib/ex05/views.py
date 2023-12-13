from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from d06_lib.helper import movies_list
from .models import Movies
from .form import RemoveForm
from django import db

# Create your views here.

def populate(request):
	result = []
	for movie in movies_list:
		try :
			ep = Movies(**movie)
			ep.save()
			result.append(f"movie - {movie['episode_nb']}: Ok!")
		except Exception as e:
			result.append(f"movie - {movie['episode_nb']}: {e}")
	return HttpResponse("<br/>".join(result[i] for i in range(len(result))))

def display(request):
	table = Movies.objects.all()
	try:
		if (not len(table)):
			raise Movies.DoesNotExist
	except Movies.DoesNotExist as e:
		return HttpResponse("No available Movies")
	return render(request, 'ex03/display.html', {"movies": table})

class remove(View):
	def get(self, request):
		try:
			movies = Movies.objects.all()
			if (not len(movies)):
				raise Exception("No data Available")
		except Exception as e:
			return HttpResponse(e)
		choices = ((movie.title, movie.title) for movie in movies)
		context = {"form": RemoveForm(choices)}
		return render(request, "ex05/remove.html", context)

	def post(self, request):
		try:
			movies = Movies.objects.all()
			if (not len(movies)):
				raise Exception("No data Available")
		except Exception as e:
			return HttpResponse(e)
		choices = ((movie.title, movie.title) for movie in movies)
		data = RemoveForm(choices, request.POST)
		if data.is_valid():
			try:
				Movies.objects.get(title=data.cleaned_data['title']).delete()
			except db.Error as e:
				print(e)
		return HttpResponseRedirect(request.path)