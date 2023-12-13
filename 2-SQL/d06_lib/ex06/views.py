from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from d06_lib.helper import sql_table_name, get_db_conn
from ex00 import views as views0
from django.http import HttpRequest
from django.views import View
from .form import UpdateForm

# Create your views here.
def init(request):
	table_name = sql_table_name(request)
	views0.init(request)

	try:
		db = get_db_conn()
		with db.cursor() as cursor:
			try:
				cursor.execute(f"""
					ALTER TABLE {table_name}
					  ADD COLUMN IF NOT EXISTS created TIMESTAMP DEFAULT now();
					ALTER TABLE {table_name}
					  ADD COLUMN IF NOT EXISTS updated TIMESTAMP DEFAULT now();
					CREATE OR REPLACE FUNCTION update_changetimestamp_column()
					  RETURNS TRIGGER AS $$
						BEGIN
						  NEW.updated = now();
						  NEW.created = OLD.created;
						  RETURN NEW;
						END;
					  $$ language 'plpgsql';
					CREATE OR REPLACE TRIGGER update_films_changetimestamp BEFORE UPDATE
					  ON {table_name} FOR EACH ROW EXECUTE PROCEDURE update_changetimestamp_column();
					""")
			except Exception as e:
				db.rollback()
				raise Exception(e)
			db.commit()
		return HttpResponse("Ok !")
	except Exception as e:
		return HttpResponse(e)
	

class update(View):
	
	def get(self, request):
		table_name = sql_table_name(request)
		try:
			db = get_db_conn()
			with db.cursor() as cur:
				cur.execute(f"SELECT * FROM {table_name};")
				table = cur.fetchall()
			if (not len(table)):
				raise Exception("No data availale")
			context = {'form': UpdateForm(choices=(
				(movie[0], movie[0]) for movie in table))}
			return render(request, "ex06/update.html", context)
		except Exception as e:
			return HttpResponse(e)

	def post(self, request: HttpRequest):
		table_name = sql_table_name(request)
		try:
			db = get_db_conn()
			title = request.POST.get('title')
			opening_crawl = request.POST.get('opening_crawl')
			with db.cursor() as cur:
				cur.execute(f"UPDATE {table_name} SET opening_crawl = '{opening_crawl}' WHERE title = '{title}' ;")
				db.commit()
		except Exception as e:
			print(e)
		return HttpResponseRedirect(request.path)
	