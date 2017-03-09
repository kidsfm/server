from django.conf.urls	import url
from .views 			import Index, Programs, Programs_json


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
			Programs,
			name='programs'
	),


	# /schedule/programs/
	# /schedule/programs?<offset=0&limit=4>
	url(
			r'^programs/$',
			Programs_json.as_view(),
			name='programs_json'
	),

]