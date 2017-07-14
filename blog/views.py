from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render
from datetime				import datetime
from .models				import Article



class Index(View):
	'''
	Returns an HTML page with an index of Article objects

	URL:	/blog/
	'''
	def get(self, request):

		# define theme settings/properties
		template_uri = 'blog/index.html'


		# fetch all data from Article model
		article_data = fetch_article_data({})


		# load data in context container
		context = {
			"articles"	: article_data,
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)




class Articles(View):
	'''
	Returns an HTML page with details of a single Article object

	URL:	/blog/articles/<article-slug>
	'''
	def get(self, request, article_slug):

		# define theme settings/properties
		template_uri = 'blog/post.html'


		# fetch data from Article model
		article_data = fetch_article_data({'slug':article_slug}).first()


		# load data in context container
		context = {
			"article"	: article_data,
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)




class Articles_json(View):
	'''
	Returns serialized JSON data enabling client to filter blog.Article objects via URL-encoded queries.

	URL: 	
	- /blog/articles/
	- /blog/articles?<offset=0&limit=4&slug=article-slug>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query params
		query = {
			"slug"	 : request.GET.get('slug', None),
			"offset" : request.GET.get('offset', None),
			"limit"	 : request.GET.get('limit', None)
		}



		# fetch data
		article_data = fetch_article_data(query)


		# serialize & return data
		data = serializers.serialize(
										'json', 
										list(article_data), 
										fields=(
												'title',
												'content',
												'author',
												'published_on',
												'slug',
												)
									)
		return HttpResponse(data, content_type="application/json")



def fetch_article_data(query):
	'''
	Helper function that queries the DB for Article objects using filters defined in query.
	'''

	# fetch slug
	kwargs = dict()
	try:
		if query['slug'] is not None:
			kwargs['slug__icontains'] = query['slug']
	except:
		pass
	

	# fetch article data from DB
	articles = Article.objects.filter( **kwargs )


	# apply offset
	try:
		offset = int(query['offset'])
		articles = articles[offset:]
	except:
		pass
		

	# apply limit
	try:
		limit = int(query['limit'])
		articles = articles[:limit]
	except:
		pass


	# return data
	return articles








	