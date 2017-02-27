from django.db 	import models
from django 	import forms



class Member(models.Model):
	'''
	Member model
	defines attributes for a single Member object of the Team app
	'''
	first_name		= models.CharField(max_length=50)
	middle_name		= models.CharField(max_length=50,blank=True)
	last_name		= models.CharField(max_length=50)
	bio				= models.TextField()
	profile_img		= models.ImageField(upload_to='img/profile/')
	interests		= models.ManyToManyField('Interests')
	role 			= models.ForeignKey('Role', on_delete=models.CASCADE, default=1)
	media_url		= models.URLField(max_length=200)
	portfolio_url	= models.URLField(max_length=200)

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









