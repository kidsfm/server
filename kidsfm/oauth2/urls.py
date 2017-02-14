from django.conf.urls	import url
from oauth2.views 		import Index, Flickr, Youtube


urlpatterns = [
	# /
	url(r'^$', 			Index.as_view(), 		name='Index'),

	# /flickr
	url(r'^flickr/', Flickr.as_view(), 	name='Flickr'),

	# /youtube
	url(r'^youtube/', 	Youtube.as_view(), 		name='Youtube'),
]