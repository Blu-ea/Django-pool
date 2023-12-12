from django.shortcuts import render
from d06_lib.helper import get_db_conn , movies, sql_table_name
from django.http import HttpResponse
import psycopg2

# Create your views here.
def populate(request):
	try:
		table_name = sql_table_name(request)
		db = get_db_conn()
		INSERT_DATA = f"""
		INSERT INTO {table_name}
		(
			episode_nb,
			title,
			director,
			producer,
			release_date
		)
		VALUES
		(
			%s, %s, %s, %s, %s
		);
		"""
		result = []
		with db.cursor() as curs:
			for movie in movies:
				try:
					curs.execute(INSERT_DATA, (
						movie['episode_nb'],
						movie['title'],
						movie['director'],
						movie['producer'],
						movie['release_date'],
					))
					result.append(f"movie - {movie['episode_nb']} : OK")
					db.commit()
				except psycopg2.DatabaseError as e:
					db.rollback()
					result.append(f"movie - {movie['episode_nb']} : {e}")
		return HttpResponse("<br/>".join(str(i) for i in result))
	except Exception as e:
		return HttpResponse(e)
	
def display(request):
	try:
		table_name = sql_table_name(request)
		db = get_db_conn()
		with db.cursor() as cur:
			cur.execute(f"SELECT * FROM {table_name};")
			table = cur.fetchall()
		if (not len(table)):
			raise Exception()
		return render(request, "ex02/display.html", {"movies": table})
	except Exception as e:
		return HttpResponse(f"No data available !<br/>{e}")