from django.conf.urls	import url
from . 					import views


urlpatterns = [

	# /team/
	url(r'^$', 								views.Index, 	name='index'),

	# /team/<member-slug>
	url(r'^(?P<member_slug>[\w\-]+)/$', 	views.Member, 	name='member'),
]