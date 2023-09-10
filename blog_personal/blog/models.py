from django.db import models

# Create your models here.
class Models(models.Model):
	title = models.CharField(max_lenght=200)
	content = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.title
