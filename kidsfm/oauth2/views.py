from django.http					import HttpResponse
from django.template				import loader
from django.views.generic			import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json






@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
	def get(self, request):
		return HttpResponse('I am called from a get Request')
	
	def post(self, request):
		post_data = request.POST
		return HttpResponse(json.dumps(post_data), content_type="application/json")