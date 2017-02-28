from django.db 						import models
from django 						import forms
from django_extensions.db.fields 	import AutoSlugField



class Member(models.Model):
	'''
	Member model
	defines attributes for a single Member object of the Team app
	'''
	first_name		= models.CharField(max_length=50)
	middle_name		= models.CharField(max_length=50,blank=True)
	last_name		= models.CharField(max_length=50)
	bio				= models.TextField()

	# ToDo
	# - find a way to overwrite profile images instead of duplicating them
	# see: http://stackoverflow.com/a/8342249
	profile_img		= models.ImageField(upload_to='img/team/profile')

	interests		= models.ManyToManyField('Interests')
	role 			= models.ForeignKey('Role', on_delete=models.CASCADE, default=1)
	email			= models.EmailField(blank=True)
	portfolio		= models.URLField(max_length=300,blank=True)
	social_media	= models.URLField(max_length=300,blank=True)

	# ToDo
	# - generate slug auto-magically
	# see: https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.SlugField
	# see: https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields
	slug 			= AutoSlugField(
							#'slug', 
							max_length=101, 
							unique=True, 
							#default=uuid.uuid4,
							populate_from=('first_name','last_name')
						)

	def __str__(self):
		return '%s %s %s' % (self.first_name, self.middle_name ,self.last_name)



class Role(models.Model):
	'''
	Role model
	container for user defined roles i.e. host, director etc for a Member object of the Team app
	'''
	label		= models.CharField(max_length=50)
	description	= models.CharField(max_length=200)

	# ToDo:
	#icon		= create & import icon choices from pages app

	# ToDo:
	#color		= create & import color choices from pages app

	def __str__(self):
		return self.label



class Interests(models.Model):
	'''
	Interests model
	defines possible interests for a Member object of the Team app
	'''
	label		= models.CharField(max_length=50)
	description = models.CharField(max_length=200,blank=True)

	def __str__(self):
		return self.label









