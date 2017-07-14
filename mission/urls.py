from django.conf.urls	import url
from .views 			import Index, Statements, Statements_json


urlpatterns = [

	# /mission/
	url(
			r'^$',
			Index.as_view(),
			name='index'
	),

    # /mission/statements/<statement-slug>
    url(
			r'^statements/(?P<statement_slug>[\w\-]+)/$',    
			Statements.as_view(),
			name='statements'
    ),


	# /mission/statements/
	# /mission/statements?<id=1&slug=some-slug&offset=0&limit=4>
	url(
			r'^statements/$',
			Statements_json.as_view(),
			name='members_json'
	),
]



