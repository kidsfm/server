from django.conf.urls	import url
from oauth2.views 		import Index, Instagram, Youtube


urlpatterns = [
	# /
	url(r'^$', 			Index.as_view(), 		name='Index'),

	# /instagram
	# ToDo: How to retreive code from url?
	# http://your-redirect-uri?code=CODE
	# see: https://www.instagram.com/developer/authentication/
	url(r'^instagram/', Instagram.as_view(), 	name='Instagram'),

	# /youtube
	url(r'^youtube/', 	Youtube.as_view(), 		name='Youtube'),
]