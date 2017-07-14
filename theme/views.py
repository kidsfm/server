from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render



class Index(View):
	'''
	Returns an HTML page with an idex of theme.XXXXXXX objects.

	URL:	/theme/
	'''
	def get(self, request):

		# define theme settings/properties
		template_uri = 'theme/index.html'
		

		# placeholder template
		template 	= loader.get_template(template_uri)
		context 	= {}
		return HttpResponse(template.render(context,request))




	
	










