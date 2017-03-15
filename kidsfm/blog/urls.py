from django.conf.urls	import url
from .views 			import Index, Article


urlpatterns = [

	# /blog/
	url(
			r'^$',
			Index,
			name='index'
	),

	# /blog/<article-slug>
	url(
			r'^(?P<article_slug>[\w\-]+)/$',
			Article,
			name='article'
	),
]





