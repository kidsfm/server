from django.conf.urls	import url
from .views 			import Index, Programs, Programs_json, Timeslots_json


urlpatterns = [

	# /schedule/
	url(
			r'^$',
			Index.as_view(),
			name='index'
	),


	# /schedule/<program-slug>
	url(
			r'^programs/(?P<program_slug>[\w\-]+)/$',
			Programs.as_view(),
			name='programs'
	),


	# /schedule/programs/
	# /schedule/programs?<offset=0&limit=4&slug=program-slug>
	url(
			r'^programs/$',
			Programs_json.as_view(),
			name='programs_json'
	),


	# /schedule/timeslots/
	# /schedule/timeslots?<offset=0&limit=4&program-id=1>
	url(
			r'^timeslots/$',
			Timeslots_json.as_view(),
			name='timeslots_json'
	),

]