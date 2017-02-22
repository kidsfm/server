from django.http		import HttpResponse
from django.template	import loader


def Index(request):
	template 	= loader.get_template('team/index.html')
	context 	= {}
	return HttpResponse(template.render(context,request))


def Member(request, member_slug):
	'''
	Single member recheable from /team/<member-slug> URL
	'''
	template 	= loader.get_template('team/member.html')
	context 	= {}
	return HttpResponse(template.render(context,request))



