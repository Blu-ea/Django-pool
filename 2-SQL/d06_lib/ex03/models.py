from django.db import models
from datetime import date

# Create your models here.
class Movies(models.Model):

	class meta:
		db_table = "ex03_movies"

	title = models.CharField(max_length=64)
	episode_nb = models.PositiveIntegerField(primary_key=True,serialize=True)
	opening_crawl = models.TextField(null=True)
	director = models.CharField(max_length=32)
	producer = models.CharField(max_length=128)
	release_date = models.DateField(default=date.today)

	def __str__(self) -> str:
		return self.title