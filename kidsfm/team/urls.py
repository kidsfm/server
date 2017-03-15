from django.conf.urls	import url
from .views 			import Index, Members, Members_json, Interests_json, Roles_json


urlpatterns = [

	# /team/
	url(
			r'^$',
			Index.as_view(),
			name='index'
	),


	# /team/members/<member-slug>
	url(
			r'^members/(?P<member_slug>[\w\-]+)/$',
			Members.as_view(), 
			name='member'
	),


	# /team/members/
	# /team/members?<role=1&offset=0&limit=4>
	url(
			r'^members/$',
			Members_json.as_view(),
			name='members_json'
	),


	# /team/interests/
	# /team/interests?<id=1&label=host>
	url(
			r'^interests/$',
			Interests_json.as_view(),
			name='interests_json'
	),


	# /team/roles/
	# /team/roles?<id=1&label=host&member-id=2>
	url(
			r'^roles/$',
			Roles_json.as_view(),
			name='roles_json'
	),
]



