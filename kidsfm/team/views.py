from django.http		import HttpResponse
from django.template	import loader


def Index(request):
	'''
	ToDo:
	- decouple the team app from the design theme????
	- this view should simply return JSON data to the an Angular controller
	- update Routes to serve html from pages.View in response to /team/ url
	- it should be queryable i.e. /team?<amount_per_category>=4
	'''
	template 	= loader.get_template('team/index.html')
	context 	= {}
	return HttpResponse(template.render(context,request))


def Members(request, member_slug):
	'''
	Single member recheable from /team/<member-slug> URL
	'''
	template 	= loader.get_template('team/member.html')
	context 	= {}
	return HttpResponse(template.render(context,request))


def Members_json():
	pass



