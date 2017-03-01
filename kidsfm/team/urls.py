from django.conf.urls	import url
from .views 			import Index, Members, Members_json, Interests_json


urlpatterns = [

	# /team/
	url(
			r'^$',
			Index,
			name='index'
	),


	# /team/members/<member-slug>
	url(
			r'^members/(?P<member_slug>[\w\-]+)/$',
			Members, 
			name='member'
	),


	# /team/members?<q1=arg1&q2=arg2>
	url(
			r'^members/$',
			Members_json.as_view(),
			name='members_json'
	),


	# /team/interests?<q1=arg1&q2=arg2>
	url(
			r'^interests/$',
			Interests_json.as_view(),
			name='interests_json'
	),
]



