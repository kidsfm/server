from django.conf.urls	import url
from .views 			import Index, Articles, Articles_json


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


	# /blog/articles/
	# /blog/articles?<offset=0&limit=4&slug=article-slug>
	url(
			r'^articles/$',
			Articles_json.as_view(),
			name='articles_json'
	),
]





