from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from d06_lib import settings
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.

def index(request :WSGIRequest):
	table_name = ''
	if (request.path == '/ex00/init/'):
		table_name = "ex00_movies"
	elif (request.path == '/ex02/init/'):
		table_name = "ex02_movies"
	else: return HttpResponse(f"'{request.path}'")
	try:
		param = settings.DATABASES["default"]
		db = psycopg2.connect(f"\
						dbname={param['NAME']}\
						user={param['USER']}\
						password={param['PASSWORD']}\
						host={param['HOST']}\
						port={param['PORT']}")
		with db.cursor() as cursor:
			cursor.execute(f"""
				  CREATE TABLE IF NOT EXISTS {table_name}(
					title varchar(64) UNIQUE NOT NULL,
					episode_nb serial PRIMARY KEY,
					opening_crawl text,
					director varchar(32) NOT NULL,
					producer varchar(128) NOT NULL,
					release_date date NOT NULL
				  );
				""")
			cursor.commit()
		return (HttpResponse("Ok !"))
	except Exception as e:
		return HttpResponse(e)