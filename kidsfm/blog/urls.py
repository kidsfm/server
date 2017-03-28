from django.conf.urls	import url
from .views 			import Index, Articles


urlpatterns = [

	# /blog/
	url(
			r'^$',
			Index.as_view(),
			name='index'
	),

	# /blog/articles/<article-slug>
	url(
			r'^articles/(?P<article_slug>[\w\-]+)/$',
			Articles.as_view(),
			name='article'
	),
]





