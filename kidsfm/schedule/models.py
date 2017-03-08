from django.db 		import models
from team.models	import Member



class Program(models.Model):
	'''
	Program model
	defines attributes for a single Program object of the Schedule app
	'''
	title		= models.CharField(max_length=50)
	description	= models.TextField(max_length=255)
	start_time 	= models.DateTimeField()
	duration	= models.DurationField()
	start_date	= models.DateField()
	end_date	= models.DateField()
	frequency	= models.ManyToManyField('Day')
	team		= models.ManyToManyField(Member)
	


	# ToDo:
	# - create & import icon choices from theme app
	#icon			= 


	# ToDo:
	# - create & import color choices from theme app
	#color			= 


	def __str__(self):
		return '%s: %s...' % (self.title, self.description[:10])



class Day(models.Model):
	'''
	Day model
	defines attributes for a single Day object of the Schedule app
	'''
	label		= models.CharField(max_length=50)








