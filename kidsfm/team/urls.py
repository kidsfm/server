from django.conf.urls	import url
from .views 			import Index, Members, Members_json


urlpatterns = [

	# /team/
	# returns an HTML page with an index of team.Member objects
	url(r'^$', 									Index, 		name='index'),


	# /team/members/<member-slug>
	# returns an HTML page with details of a single team.Member object
	url(r'^members/(?P<member_slug>[\w\-]+)/$', Members, 		name='member'),


	# /team/members?<query>
	# returns serialized JSON data. enables client to filter team.Member objects
	#url(r'^members?(?P<query>[\w\=\&]+)$', 		Members_json.as_view(), name='members_json'),
	url(r'^members/$', 		Members_json.as_view(), name='members_json'),
]



