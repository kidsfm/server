import json
from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from .models				import Member



def Index(request):
	'''
	ToDo:
	- implement this
	'''
	template 	= loader.get_template('team/index.html')
	context 	= {}
	return HttpResponse(template.render(context,request))



def Members(request, member_slug):
	'''
	URL:	/team/members/<member-slug>
	Desc:	returns an HTML page with details of a single team.Member object


	ToDo:
	- implement this
	'''
	template 	= loader.get_template('team/member.html')
	context 	= {}
	return HttpResponse(template.render(context,request))



class Members_json(View):
	'''
	URL: 	/team/members?<query>
	Returns serialized JSON data. enables client to filter team.Member objects via URL-encoded queries.

	ToDo:
	- this view should simply return JSON data to the an Angular controller
	'''
	def get(self, request):

		# fetch query from body
		#query = request.GET['query']
		query = 'role=1&offset=0&limit=4'

		# Debug
		print('Now in team.views.Members_json.get')
		print('query is: ', query)
		
		# init member list
		member_list = []

		# fetch data
		members = fetch_member_data(query)

		# serialize & return data
		#for member in members:
		#	member_list.append(member)
		data = serializers.serialize(
										'json', 
										list(members), 
										fields=(
													'first_name',
													'middle_name',
													'last_name',
													'bio',
													'profile_img',
													'role',
													'email',
													'portfolio',
													'social_media',
													'slug',
													'interests'
												)
									)
		return HttpResponse(data, content_type="application/json")



def fetch_member_data(query):
	'''
	Helper function that fetches data using filters defined in query.

	ToDo:
	- this view should simply queries the DB using provided filters and returns Python data

	See: 
	- https://docs.djangoproject.com/en/1.10/topics/db/queries/#retrieving-specific-objects-with-filters
	- https://docs.djangoproject.com/en/1.10/topics/db/queries/#field-lookups
	- http://www.nomadjourney.com/2009/04/dynamic-django-queries-with-kwargs/
	'''

	# de-serialize query into a dictionary
	q_dict = dict(item.split("=") for item in query.split("&"))


	# fetch query components to construct keyword args dict
	kwargs = dict()
	# first name
	try:
		kwargs['first_name__icontains'] = q_dict['fname__icontains']
	except:
		pass
	# middle name
	try:
		kwargs['middle_name__icontains'] = q_dict['mname']
	except:
		pass
	# last name
	try:
		kwargs['last_name__icontains'] = q_dict['lname']
	except:
		pass
	# role
	try:
		kwargs['role'] = int(q_dict['lname'])
	except:
		pass
	

	# fetch data from DB
	members = Member.objects.filter( **kwargs )


	# return results
	return members
	
	










