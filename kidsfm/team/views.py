from django.http			import HttpResponse
from django.template		import loader
from django.views.generic	import View
from django.core 			import serializers
from django.shortcuts		import render
from .models				import Member, Interest, Role



class Index(View):
	'''
	Returns an HTML page with an idex of team.Member objects.

	URL:	/team/
	'''
	def get(self, request):

		# define theme settings/properties
		template_uri = 'team/index.html'


		# fetch all data from Member model
		member_data = fetch_member_data({})


		# fetch all data from Interest model
		interest_data = fetch_interest_data({})


		# fetch all data from Role model
		role_data = fetch_role_data({})


		# load data in params container
		params 				= dict()
		params["members"]	= member_data
		params["interests"] = interest_data
		params["roles"] 	= role_data


		# render template with data & send HTML to client
		return render(request, template_uri, params)

		



class Members(View):
	'''
	Returns an HTML page with details of a single team.Member object.

	URL:	/team/members/<member-slug>

	ToDo:
	- implement this
	'''
	def get(self, request, member_slug):

		# define theme settings/properties
		template_uri = 'team/member.html'


		# fetch all data from Member model
		member_data 	= fetch_member_data({'slug':member_slug})
		member_values 	= member_data.values()[0]


		# fetch all data from Interest model
		interest_data 	= fetch_interest_data({})
		interest_values = interest_data.values()


		# fetch all data from Role model
		role_data 		= fetch_role_data({})
		role_values 	= role_data.values()


		# load data in params container
		params 					= dict()
		params['first_name']	= member_values['first_name']
		params['middle_name']	= member_values['middle_name']
		params['last_name']		= member_values['last_name']
		params['bio']			= member_values['bio']
		params['profile_img']	= member_values['profile_img']
		params['email']			= member_values['email']
		params['portfolio']		= member_values['portfolio']
		params['social_media']	= member_values['social_media']
		params['slug']			= member_values['slug']

		# ToDo:
		# update fetch_role_data() to enable client to query a member's role
		params['role']			= role_values[member_values['role_id']]['label']


		# ToDo:
		# update fetch_interest_data() to enable client to query a member's interests
		#params['interest']		= member_values['interest_id']


		# Debug
		print('\tnow in team.views.Member()')
		print('\tmember-slug is: %s' % (member_slug,))
		print('\tfetched member_data: %s' % (member_data,))
		print('\tfirst name is: %s' % (params["first_name"],))
		


		# render template with data & send HTML to client
		return render(request, template_uri, params)



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

	# fetch slug
	try:
		kwargs['slug__icontains'] = query['slug']
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
	
	










