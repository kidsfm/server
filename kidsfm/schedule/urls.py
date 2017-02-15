from django.conf.urls	import url
from . 					import views


urlpatterns = [

	# /schedule/
	url(r'^$', 								views.Index, 	name='index'),

	# /schedule/<program-slug>
	url(r'^(?P<program_slug>[\w\-]+)/$', 	views.Program, 	name='program'),
]