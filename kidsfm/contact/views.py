from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render



class Index(View):
	'''
	Returns an HTML page with a contact form

	URL:	/contact/
	'''
	def get(self, request):

		# define theme settings/properties
		template_uri = 'contact/index.html'


		# fetch all data from Statement model
		#statement_data = fetch_statement_data({})


		# load data in context container
		#context = {"statements": statement_data}
		context = {}


		# render template with data & send HTML to client
		return render(request, template_uri, context)



	def post(self, request):
		pass



