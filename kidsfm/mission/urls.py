from django.conf.urls	import url
from .views 			import Index, Statement


urlpatterns = [

	# /mission/
	url(
			r'^$',
			Index.as_view(),
			name='index'
	),

    # /mission/<statement-slug>
    url(
			r'^(?P<statement_slug>[\w\-]+)/$',    
			Statement.as_view(),
			name='statement'
    ),
]



