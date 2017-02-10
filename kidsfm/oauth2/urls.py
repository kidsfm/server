from django.conf.urls	import url
from oauth2.views 		import Index


urlpatterns = [
	# /
	url(r'^$', Index.as_view(), name='Index'),
]