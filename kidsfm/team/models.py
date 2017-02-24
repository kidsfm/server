from django.db import models



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

	def __str__(self):
		return self.label



class Member(models.Model):
	'''
	Member model
	defines attributes for a single Member object of the Team app
	'''

	first_name		= models.CharField(max_length=100)
	middle_name		= models.CharField(max_length=100)
	last_name		= models.CharField(max_length=100)
	bio				= models.TextField()
	profile_img		= models.ImageField(
										upload_to='/profile_images/'
									)

	# ToDo:
	# - implement minimum & maximum interest for each Member
	# - see: http://stackoverflow.com/a/15096984
	intrests		= models.ForeignKey(
										Interests,
										on_delete=models.CASCADE
									)

	# ToDo:
	# - should role be a OneToOneField instead?
	# - see: https://docs.djangoproject.com/en/1.10/ref/models/fields/#onetoonefield
	role 			= models.ForeignKey(
										Role,
										on_delete=models.CASCADE
									)

	media_url		= models.URLField(max_length=200)
	portfolio_url	= models.URLField(max_length=200)

	def __str__(self):
		return '%s %s %s' % (self.first_name, self.middle_name ,self.last_name)





