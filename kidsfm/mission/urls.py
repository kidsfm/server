from django.conf.urls	import url
from .views 			import Index


urlpatterns = [

	# /mission/
	url(
			r'^$',
			Index.as_view(),
			name='index'
	),
]



