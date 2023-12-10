from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	step = 255 / 50
	context = {
		"range": [
			"{:02X}".format(int(i * step)) for i in range(50)
		]
	}
	return render(request, "ex03/index.html", context)