from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import History
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings
import logging


# Create your views here.

def index(request: WSGIRequest):
	logger = logging.getLogger("ex02")

	if (request.method == "POST"):
		my_form = History(request.POST)
		if my_form.is_valid():
			logger.info(my_form.cleaned_data['history'])
		return(HttpResponseRedirect("/ex02/"))
	try:
		f = open(settings.HISTORY_LOG_FILE, 'r')
		historys = [line for line in f.readlines()]
	except:
		historys = []
	return (render(request ,"ex02/index.html",{"form": History(), 'historys': historys}))