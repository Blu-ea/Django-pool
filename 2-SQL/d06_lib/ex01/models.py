from django.db import models

# Create your models here.
class Movies(models.Model):
	title = models.CharField(max_length=64)
	episode_nb = models.PositiveIntegerField(primary_key=True,serialize=True	)
	opening_crawl = models.TextField(null=True)
	director = models.TextField(max_length=32)
	producer = models.TextField(max_length=128)
	
	def __str__(self) -> str:
		return self.title