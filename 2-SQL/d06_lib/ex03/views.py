from django.shortcuts import render, HttpResponse
from d06_lib.helper import movies_list
from .models import Movies

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