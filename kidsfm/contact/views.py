from django.http			import HttpResponse, HttpResponseRedirect
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render
from datetime				import datetime
from .models				import Message, Location
from .forms					import MessageForm



class Index(View):
	'''
	Returns an HTML page with a contact form

	URL:	/contact/
	'''
	def get(self, request):

		# define theme settings/properties
		template_uri = 'contact/index.html'


		# init contact form
		form = MessageForm()


		# fetch Location data
		location_data = Location.objects.all()


		# load data in context container
		context = {
			'form'		: form,
			'locations' : location_data
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)



	def post(self, request):

		form = MessageForm(request.POST)
		if form.is_valid():

			# theme settings/properties
			template_uri = 'contact/thankyou.html'


			# fetch Message data from form
			name 	= form.cleaned_data['name']
			email 	= form.cleaned_data['email']
			message = form.cleaned_data['message']
			

			# Debug
			print('\treceived valid search form')
			print('\tname is:',name)
			print('\temail is:',email)
			print('\tmessage is:',message)


			# ToDo:
			# - commit message to DB
			new_message = Message(
									name=name,
									email=email,
									message=message,
									sent_date=datetime.now()
								)
			new_message.save()


			# ToDo:
			# verify that new message is in DB


			# load data in context container
			context = {
				'message':new_message
			}


			# render template with data & send HTML to client
			return render(request, template_uri, context)

		else:
			HttpResponseRedirect("/contact/")




		




