from django.db 						import models
from django_extensions.db.fields 	import AutoSlugField
from team.models					import Member



class Article(models.Model):
	'''
	Article model
	defines attributes for a single Article object of the Blog app
	'''
	title		= models.CharField(max_length=50,unique=True)
	content		= models.TextField()

	# ToDo
	# - find a way to overwrite profile images instead of duplicating them
	# see: http://stackoverflow.com/a/8342249
	image		= models.ImageField(upload_to='img/blog/article')

	author		= models.ForeignKey(
						Member, 
						on_delete=models.CASCADE
	)
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
	#
	# - sanetize slug using: from django.utils.text import slugify
	#	see: https://keyerror.com/blog/automatically-generating-unique-slugs-in-django
	#	see: https://docs.djangoproject.com/en/1.10/ref/utils/#module-django.utils.text
	#
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
		return '%s: %s...' % (self.title, self.content[:10])







