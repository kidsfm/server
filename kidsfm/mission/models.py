from django.db 						import models
from django_extensions.db.fields 	import AutoSlugField



class Statement(models.Model):
	'''
	Statement model
	defines attributes for a single Statement object of the Mission app
	'''
	def __str__(self):
		#return '%s %s %s' % (self.first_name, self.middle_name ,self.last_name)
		pass








