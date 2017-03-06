from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render
from .models				import Statement



class Index(View):
	'''
	Returns an HTML page with an idex of mission.Statement objects.

	URL:	/mission/
	'''
	def get(self, request):

		# define theme settings/properties
		template_uri = 'mission/index.html'


		# fetch all data from Statement model
		statement_data = fetch_statement_data({})


		# load data in context container
		context = {"statements": statement_data}


		# render template with data & send HTML to client
		return render(request, template_uri, context)



class Statements(View):
	'''
	Returns an HTML page with details for a single mission.Statement object.

	URL:	/mission/<statement-slug>
	'''
	def get(self, request, statement_slug):

		# define theme settings/properties
		template_uri = 'mission/statement.html'


		# fetch all data from Statement model
		statement_data = fetch_statement_data({"slug":statement_slug}).first()


		# load data in context container
		context = {"statement": statement_data}


		# render template with data & send HTML to client
		return render(request, template_uri, context)






class Statements_json(View):
	'''
	Returns serialized JSON data enabling client to filter mission.Statement objects via URL-encoded queries.

	URL: 	
	- /mission/statements/
	- /mission/statements?<id=1&slug=some-slug&offset=0&limit=4>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query context
		q_dict = dict()
		q_dict['id'] 		= request.GET.get('id', None)
		q_dict['offset'] 	= request.GET.get('offset', None)
		q_dict['limit'] 	= request.GET.get('limit', None)


		# fetch data
		statement_data 		= fetch_statement_data(q_dict)


		# serialize & return data
		data = serializers.serialize(
										'json', 
										list(statement_data), 
										fields=(
													'title',
													'description',
													'image',
												)
									)
		return HttpResponse(data, content_type="application/json")



def fetch_statement_data(query):
	'''
	Helper function that queries the DB for Statement objects using filters defined in query.
	'''

	# fetch id
	kwargs = dict()
	try:
		kwargs['id'] = int(query['id'])
	except:
		pass

	# fetch slug
	try:
		kwargs['slug__icontains'] = query['slug']
	except:
		pass
	

	# fetch Statement data from DB
	statements = Statement.objects.filter( **kwargs )


	# apply offset
	try:
		offset = int(query['offset'])
		statements = statements[offset:]
	except:
		pass
		

	# apply limit
	try:
		limit = int(query['limit'])
		statements = statements[:limit]
	except:
		pass


	# return data
	return statements




	
	










