from django.db 	import models
from django 	import forms



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
										upload_to='img/profile/'
									)

	# ToDo:
	# - implement minimum & maximum interest for each Member
	# - see: http://stackoverflow.com/a/15096984
	interests		= models.ManyToManyField(Interests)



	# ToDo:
	# - should role be a OneToOneField or ManyToManyField?
	# - see: https://docs.djangoproject.com/en/1.10/ref/models/fields/#onetoonefield
	role 			= models.ManyToManyField(Role)

	media_url		= models.URLField(max_length=200)
	portfolio_url	= models.URLField(max_length=200)




	def __str__(self):
		return '%s %s %s' % (self.first_name, self.middle_name ,self.last_name)


#	def clean_interests(self):
#	    """
#	    Check if there are at most 5 interests
#	    """
#	    # fetch data that was submitted
#	    data = self.cleaned_data['interests']
#
#	    # Debug
#	    print('user[%s] has %s interests' % (self.first_name, self.interests.count()) )
#
#	    # verify that there aren't more than 5
#	    if data.count() > 5:
#	        raise forms.ValidationError(
#	        						"A member can have at most 5 interests!",
#	        						code='invalid'
#	        						)
#	    # else return data
#	    return data
#




# On: validating that interests < 5
# see: http://stackoverflow.com/a/20230270
#
#from django.db.models.signals import m2m_changed
#from django.core.exceptions import ValidationError
#
#
#def interests_changed(sender, **kwargs):
#    if kwargs['instance'].interests.count() > 5:
#        raise ValidationError("You can't assign more than 5 interests")
#
#
#m2m_changed.connect(interests_changed, sender=Member.interests.through)






