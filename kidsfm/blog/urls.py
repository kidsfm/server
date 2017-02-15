from django.conf.urls	import url
from . 					import views


urlpatterns = [

	# /blog/
	url(r'^$', 								views.Index, 	name='index'),

	# /blog/<article-slug>
	url(r'^(?P<article_slug>[\w\-]+)/$', 	views.Article, 	name='article'),
]





