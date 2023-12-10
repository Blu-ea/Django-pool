from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index (request):
	template = loader.get_template("ex00/index.html")
	return HttpResponse(template.render( {},request))


	# return render(request=request, template_name="index.html")
	