from django.db 						import models
from django_extensions.db.fields 	import AutoSlugField



class Member(models.Model):
	'''
	Member model
	defines attributes for a single Member object
	'''
	first_name		= models.CharField(
										max_length=50
	)
	middle_name		= models.CharField(
										max_length=50,
										blank=True
	)
	last_name		= models.CharField(
										max_length=50
	)
	bio				= models.TextField()

	# ToDo
	# - find a way to overwrite profile images instead of duplicating them
	# see: http://stackoverflow.com/a/8342249
	profile_img		= models.ImageField(
										upload_to='img/team/profile'
	)

	interests		= models.ManyToManyField(
										'Interest',
										related_name='interests'
	)
	role 			= models.ForeignKey(
										'Role',
										on_delete=models.CASCADE, 
										default=1
	)
	email			= models.EmailField(
										blank=True
	)
	portfolio		= models.URLField(
										max_length=300,
										blank=True
	)
	social_media	= models.URLField(
										max_length=300,
										blank=True
	)
	slug 			= AutoSlugField(
										max_length=101, 
										unique=True, 
										populate_from=(
													'first_name',
													'middle_name',
													'last_name'
										)
	)

	def __str__(self):
		return '%s %s %s' % (self.first_name, self.middle_name ,self.last_name)



class Role(models.Model):
	'''
	Role model
	container for user defined roles i.e. host, director etc for a Member object
	'''
	label			= models.CharField(
										max_length=50
	)
	description		= models.CharField(
										max_length=200
	)


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
		return '%s' % (self.label,)



class Interest(models.Model):
	'''
	Interest model
	defines possible interest for a Member
	'''
	label		= models.CharField(
										max_length=50
	)
	description = models.CharField(
										max_length=200,
										blank=True
	)


	# ToDo:
	# - create & import icon choices from theme app
	#icon			= 


	# ToDo:
	# - create & import color choices from theme app
	#color			= 


	def __str__(self):
		return '%s' % (self.label,)









