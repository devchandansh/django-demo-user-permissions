from django.db import models

# Create your models here.

class CarModels(models.Model):
	model_name = models.CharField(max_length=100, null=True)
	model_no = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.model_name
		
class Cars(models.Model):
	"""docstring for Cars"""
	name = models.CharField(max_length=200, null=True)
	number = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name


		