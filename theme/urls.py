from django.conf.urls	import url
from .views 			import Index


urlpatterns = [

	# /theme/
	url(
			r'^$',
			Index.as_view(),
			name='index'
	),
]



