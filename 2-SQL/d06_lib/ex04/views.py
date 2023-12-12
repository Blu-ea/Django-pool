from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from d06_lib.helper import get_db_conn, sql_table_name
from .form import RemoveForm

# Create your views here.
def remove(request: HttpRequest):
	try:
		table_name = sql_table_name(request)
		db = get_db_conn()

		if (request.method == "GET"):
			with db.cursor() as cur:
				cur.execute(f"SELECT * FROM {table_name};")
				table = cur.fetchall()
			if (not len(table)):
				raise Exception("No data availale")
			context = {'form': RemoveForm(choices=(
				(movie[0], movie[0]) for movie in table))}
			return render(request, "ex04/remove.html", context)
		else:
			title = request.POST.get('title')
			with db.cursor() as cur:
				cur.execute(f"DELETE FROM {table_name} WHERE title = '{title}';")
				db.commit()
			return HttpResponseRedirect(request.path)
	except Exception as e:
		return HttpResponse(e)
