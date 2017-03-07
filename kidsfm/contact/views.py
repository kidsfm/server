from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render
from .models				import Message
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


		# load data in context container
		context = {
			'form': form
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)



	def post(self, request):

		# define theme settings/properties
		template_uri = 'contact/thankyou.html'


		# load data in context container
		context = {}


		# render template with data & send HTML to client
		return render(request, template_uri, context)
		




