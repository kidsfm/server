from django.http		import HttpResponse
from django.template	import loader


def Index(request):
	"""
	Program index recheable from /schedule/ URL
	"""
	template 	= loader.get_template('schedule/index.html')
	context 	= {}
	return HttpResponse(template.render(context,request))


def Program(request, program_slug):
	'''
	Single program recheable from /schedule/<program-slug> URL
	'''
	template 	= loader.get_template('schedule/program.html')
	context 	= {}
	return HttpResponse(template.render(context,request))



