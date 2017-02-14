from django.conf.urls	import url
from oauth2.views 		import Index, Youtube


urlpatterns = [
	# /
	url(r'^$', 			Index.as_view(), 		name='Index'),

	# /youtube
	url(r'^youtube/', 	Youtube.as_view(), 		name='Youtube'),
]