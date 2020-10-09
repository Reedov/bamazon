from django.db import models
#from apps.author.models import Author

class Author(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.name}"

class Book(models.Model):
	name = models.CharField(max_length=200)
	add_time = models.DateTimeField(auto_now_add=True)
	author = models.ManyToManyField(Author)
	prize = models.PositiveIntegerField()
	description = models.TextField(blank=True)

	def __str__(self):
		return f"{self.name}"





