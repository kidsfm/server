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
		








