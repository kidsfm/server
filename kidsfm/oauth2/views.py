from django.http					import HttpResponse
from django.template				import loader
from django.views.generic			import View
from django.views.decorators.csrf 	import csrf_exempt
from django.utils.decorators 		import method_decorator
import json






@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
	'''
	plan to use this view to print handle post redirects from oauth2 flow via url /oauth2/
	'''
	def get(self, request):
		return HttpResponse('I am called from a get Request')
	
	def post(self, request):
		post_data = request.POST
		return HttpResponse(json.dumps(post_data), content_type="application/json")




class Flickr(View):
	'''
	plan to use this view to print handle post redirects from Flickr's 
	oauth2 flow via url /oauth2/flickr/
	'''
	def get(self, request):
		return HttpResponse('I am called from a get Request')
	
	def post(self, request):
		post_data = request.POST
		return HttpResponse(json.dumps(post_data), content_type="application/json")




class Youtube(View):
	'''
	plan to use this view to print handle post redirects from Youtube's
	oauth2 flow via url /oauth2/youtube/
	'''
	def get(self, request):
		return HttpResponse('I am called from a get Request')
	
	def post(self, request):
		post_data = request.POST
		return HttpResponse(json.dumps(post_data), content_type="application/json")











