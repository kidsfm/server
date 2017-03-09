from django.db 						import models
from django_extensions.db.fields 	import AutoSlugField
from team.models					import Member



class Program(models.Model):
	'''
	Program model
	defines attributes for a single Program object of the Schedule app
	'''
	title		= models.CharField(max_length=50,unique=True)
	description	= models.TextField()

	# ToDo
	# - find a way to overwrite profile images instead of duplicating them
	# see: http://stackoverflow.com/a/8342249
	image		= models.ImageField(upload_to='img/schedule/program')

	start_time 	= models.TimeField()
	end_time	= models.TimeField()
	start_date	= models.DateField()
	end_date	= models.DateField()
	frequency	= models.ManyToManyField('Day')
	team		= models.ManyToManyField(Member)
	slug 		= AutoSlugField(
						max_length=50, 
						unique=True, 
						populate_from=('title')
					)
	


	# ToDo:
	# - create & import icon choices from theme app
	#icon			= 


	# ToDo:
	# - create & import color choices from theme app
	#color			= 


	# ToDo:
	# - verify that end_time is scheduled after start_time
	# - verify that end_date is scheduled after start_date
	#def save(self, *args, **kwargs):
	#	if self.is_primary:
	#		try:
	#			temp = Location.objects.get(is_primary=True)
	#			if self != temp:
	#				temp.is_primary = False
	#				temp.save()
	#		except Location.DoesNotExist:
	#			pass
	#	super(Location, self).save(*args, **kwargs)


	def __str__(self):
		return '%s: %s...' % (self.title, self.description[:10])



class Day(models.Model):
	'''
	Day model
	defines attributes for a single Day object of the Schedule app
	'''
	label		= models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.label)








