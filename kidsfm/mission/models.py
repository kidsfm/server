from django.db 						import models
from django_extensions.db.fields 	import AutoSlugField



class Statement(models.Model):
	'''
	Statement model
	defines attributes for a single Statement object of the Mission app
	'''
	title			= models.CharField(max_length=50)
	description		= models.TextField()


	# ToDo
	# - find a way to overwrite images instead of duplicating them
	# - Note: image should be a square thumbnail
	# see: http://stackoverflow.com/a/8342249
	image			= models.ImageField(upload_to='img/mission/statement')


	# ToDo:
	# - create & import cover image choices from theme app
	# - Note: image should be a rectangle landscape
	#cover_image	= 


	# ToDo:
	# - create & import icon choices from theme app
	#icon			= 


	# ToDo:
	# - create & import color choices from theme app
	#color			= 


	def __str__(self):
		return '%s' % (self.title,)
		








