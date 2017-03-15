from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render
from datetime				import datetime
from .models				import Program



class Index(View):
	'''
	Returns an HTML page with an index of Program objects

	URL:	/schedule/
	'''
	def get(self, request):

		# define theme settings/properties
		template_uri = 'schedule/index.html'


		# fetch all data from Program model
		program_data = fetch_program_data({})


		# load data in context container
		context = {
			"programs"	: program_data,
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)



class Programs(View):
	'''
	Returns an HTML page with details of a single Program object

	URL:	/schedule/programs/<program-slug>
	'''
	def get(self, request, program_slug):

		# define theme settings/properties
		template_uri = 'schedule/program.html'


		# fetch all data from Program model
		program_data = fetch_program_data({'slug':program_slug}).first()


		# load data in context container
		context = {
			"program"	: program_data,
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)




class Programs_json(View):
	'''
	Returns serialized JSON data enabling client to filter schedule.Program objects via URL-encoded queries.

	URL: 	
	- /schedule/programs/
	- /schedule/programs?<offset=0&limit=4&slug=program-slug>

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
		program_data = fetch_program_data(query)


		# serialize & return data
		data = serializers.serialize(
										'json', 
										list(program_data), 
										fields=(
												'title',
												'description',
												'team',
												'slug',
												)
									)
		return HttpResponse(data, content_type="application/json")



def fetch_program_data(query):
	'''
	Helper function that queries the DB for Program objects using filters defined in query.
	'''

	# fetch slug
	kwargs = dict()
	try:
		if query['slug'] is not None:
			kwargs['slug__icontains'] = query['slug']
	except:
		pass
	

	# fetch program data from DB
	programs = Program.objects.filter( **kwargs )


	# apply offset
	try:
		offset = int(query['offset'])
		programs = programs[offset:]
	except:
		pass
		

	# apply limit
	try:
		limit = int(query['limit'])
		programs = programs[:limit]
	except:
		pass


	# return data
	return programs
	







