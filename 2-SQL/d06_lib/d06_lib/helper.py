from . import settings
import psycopg2

def get_db_conn():
	param = settings.DATABASES["default"]
	return psycopg2.connect(f"""
						dbname={param['NAME']}
						user={param['USER']}
						password={param['PASSWORD']}
						host={param['HOST']}
						port={param['PORT']}""")

movies_list = [{
			"episode_nb": 1,
			"title": "The Phantom Menace",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "1999-05-19"
		},{	"episode_nb": 2,
			"title": "Attack of the Clones",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2002-05-16"
		},{	"episode_nb": 3,
			"title": "Revenge of the Sith",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2005-05-19"
		},{	"episode_nb": 4,
			"title": "A New Hope",
			"director": "George Lucas",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1977-05-25"
		},{	"episode_nb": 5,
			"title": "The Empire Strikes Back",
			"director": "Irvin Kershner",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1980-05-17"
		},{	"episode_nb": 6,
			"title": "Return of the Jedi",
			"director": "Richard Marquand",
			"producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
			"release_date": "1983-05-25"
		},{	"episode_nb": 7,
			"title": "The Force Awakens",
			"director": "J. J. Abrams",
			"producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
			"release_date": "2015-12-11"}
	]

def sql_table_name(request):
	parse = request.path.split('/')
	if (len(parse) < 2): raise Exception(f"not know {request.path}")
	return(f"{parse[1]}_movies")