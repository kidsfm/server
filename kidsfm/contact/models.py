from django.db 						import models



class Message(models.Model):
	'''
	Message model
	defines attributes for a single Message object of the Contact app
	'''
	name		= models.CharField(max_length=100)
	email		= models.EmailField(max_length=50)
	message		= models.TextField(max_length=255)
	sent_date	= models.DateTimeField()


	def __str__(self):
		return '%s: %s...' % (self.name, self.message[:10])



class Location(models.Model):
	'''
	Location model
	defines attributes for a single Location object of the Contact app
	'''
	# meta details
	title		= models.CharField(max_length=50)
	description	= models.TextField(max_length=255)
	is_primary 	= models.BooleanField(default=False)

	# address
	address		= models.TextField(max_length=255)
	city		= models.TextField(max_length=100)
	state 		= models.TextField(max_length=100)
	country 	= models.TextField(max_length=100)

	# contact info
	phone		= models.TextField(max_length=100)
	email 		= models.EmailField(max_length=255)


	# ToDo:
	# - there can only be one primary address
	# See: http://stackoverflow.com/a/1455507
	def save(self, *args, **kwargs):
		if self.is_primary:
			try:
				temp = Location.objects.get(is_primary=True)
				if self != temp:
					temp.is_primary = False
					temp.save()
			except Location.DoesNotExist:
				pass
		super(Location, self).save(*args, **kwargs)


	def __str__(self):
		return '%s: %s...' % (self.name, self.message[:10])
		








