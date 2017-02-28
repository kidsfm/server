from django.conf.urls	import url
from . 					import views


urlpatterns = [

	# html: /team/
	url(r'^$', 									views.Index, 		name='index'),

	# html: /team/members/<member-slug>
	url(r'^members/(?P<member_slug>[\w\-]+)/$', views.Members, 	name='member'),

	# json: /team/members
	url(r'^members/?(?P<query>[\w\-]+)/$', 	views.Members_json, name='members_json'),
]