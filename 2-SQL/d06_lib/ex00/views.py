from django.shortcuts import render
from django.http import HttpResponse
from d06_lib.helper import get_db_conn
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.

def init(request :WSGIRequest):
	parse = request.path.split('/')
	if (len(parse) < 2): return HttpResponse(f"not know {request.path}")
	table_name = f"{parse[1]}_movies"

	try:
		db = get_db_conn()
		with db.cursor() as cursor:
			cursor.execute(f"""
				  CREATE TABLE IF NOT EXISTS {table_name}(
					title varchar(64) UNIQUE NOT NULL,
					episode_nb serial PRIMARY KEY,
					opening_crawl text,
					director varchar(32) NOT NULL,
					producer varchar(128) NOT NULL,
					release_date date NOT NULL
				  );""")
			db.commit()
		return HttpResponse("Ok !")
	except Exception as e:
		return HttpResponse(e)