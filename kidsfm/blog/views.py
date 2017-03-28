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
		#article_data = fetch_article_data({})


		# load data in context container
		context = {
			#"articles"	: article_data,
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
		#article_data = fetch_article_data({'slug':article_slug}).first()


		# load data in context container
		context = {
			#"article"	: article_data,
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)



	