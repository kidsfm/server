from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from .models				import Member, Interest, Role



def Index(request):
	'''
	ToDo:
	- fetch data for each model separately
	- serialize data for each model separately
	- concatenate serialized string
	- send combined data to client
	'''
	template 	= loader.get_template('team/index.html')
	context 	= {}
	return HttpResponse(template.render(context,request))



def Members(request, member_slug):
	'''
	Returns an HTML page with details of a single team.Member object.

	URL:	/team/members/<member-slug>

	ToDo:
	- implement this
	'''
	template 	= loader.get_template('team/member.html')
	context 	= {}
	return HttpResponse(template.render(context,request))



class Members_json(View):
	'''
	Returns serialized JSON data enabling client to filter team.Member objects via URL-encoded queries.

	URL: 	
	- /team/members/
	- /team/members?<q1=arg1&q2=arg2>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query params
		q_dict = dict()
		q_dict['role'] 		= request.GET.get('role', None)
		q_dict['offset'] 	= request.GET.get('offset', None)
		q_dict['limit'] 	= request.GET.get('limit', None)

		# fetch data
		member_data = fetch_member_data(q_dict)


		# serialize & return data
		data = serializers.serialize(
										'json', 
										list(member_data), 
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
													'interest',
												)
									)
		return HttpResponse(data, content_type="application/json")



def fetch_member_data(query):
	'''
	Helper function that queries the DB for Member objects using filters defined in query.

	See: 
	- https://docs.djangoproject.com/en/1.10/topics/db/queries/#retrieving-specific-objects-with-filters
	- https://docs.djangoproject.com/en/1.10/topics/db/queries/#field-lookups
	- http://www.nomadjourney.com/2009/04/dynamic-django-queries-with-kwargs/
	'''

	# fetch role
	kwargs = dict()
	try:
		kwargs['role'] = int(query['role'])
	except:
		pass
	

	# fetch Member data from DB
	members = Member.objects.filter( **kwargs )


	# apply offset
	try:
		offset = int(query['offset'])
		members = members[offset:]
	except:
		pass
		

	# apply limit
	try:
		limit = int(query['limit'])
		members = members[:limit]
	except:
		pass


	# return data
	return members



class Interests_json(View):
	'''
	Returns serialized JSON data enabling client to filter team.Interest objects via URL-encoded queries.

	URL: 	
	- /team/interests/
	- /team/interests?<q1=arg1&q2=arg2>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query params
		q_dict = dict()
		q_dict['id'] 		= request.GET.get('id', None)
		q_dict['label'] 	= request.GET.get('label', None)

		# fetch data
		interest_data = fetch_interest_data(q_dict)

		# serialize & return data
		data = serializers.serialize(
										'json', 
										list(interest_data), 
										fields=(
													'label',
													'description'
												)
									)
		return HttpResponse(data, content_type="application/json")



def fetch_interest_data(query):
	'''
	Helper function that queries the DB for Interest objects using filters defined in query.
	'''

	# fetch id
	kwargs = dict()
	try:
		kwargs['pk'] = int(query['id'])
	except:
		pass

	# fetch label
	try:
		if query['label'] is not None:
			kwargs['label__icontains'] = query['label']
	except:
		pass

	# fetch Interest data from DB
	interests = Interest.objects.filter( **kwargs )


	# return data
	return interests



class Roles_json(View):
	'''
	Returns serialized JSON data enabling client to filter team.Role objects via URL-encoded queries.

	URL: 	
	- /team/roles/
	- /team/roles?<q1=arg1&q2=arg2>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query params
		q_dict = dict()
		q_dict['id'] 		= request.GET.get('id', None)
		q_dict['label'] 	= request.GET.get('label', None)

		# fetch data
		interest_data = fetch_interest_data(q_dict)

		# serialize & return data
		data = serializers.serialize(
										'json', 
										list(interest_data), 
										fields=(
													'label',
													'description'
												)
									)
		return HttpResponse(data, content_type="application/json")



def fetch_role_data(query):
	'''
	Helper function that queries the DB for role objects using filters defined in query.
	'''

	# fetch id
	kwargs = dict()
	try:
		kwargs['pk'] = int(query['id'])
	except:
		pass

	# fetch label
	try:
		if query['label'] is not None:
			kwargs['label__icontains'] = query['label']
	except:
		pass

	# fetch Role data from DB
	roles = Role.objects.filter( **kwargs )


	# return data
	return roles
	
	










