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


		# load data in context container
		context = {
			"members"	: member_data,
			"interests" : interest_data,
			"roles"		: role_data
		}


		# render template with data & send HTML to client
		return render(request, template_uri, context)

		



class Members(View):
	'''
	Returns an HTML page with details of a single team.Member object.

	URL:	/team/members/<member-slug>
	'''
	def get(self, request, member_slug):

		# define theme settings/properties
		template_uri = 'team/member.html'


		# fetch Member data for this member
		member_data 	= fetch_member_data({'slug':member_slug}).first()


		# fetch Interest data for this member
		interest_data 	= fetch_interest_data({'member-id':member_data.id})


		# load data in context container
		context = {
			"member" 	: member_data,
			"interests" : interest_data,
		}

		# render template with data & send HTML to client
		return render(request, template_uri, context)



class Members_json(View):
	'''
	Returns serialized JSON data enabling client to filter team.Member objects via URL-encoded queries.

	URL: 	
	- /team/members/
	- /team/members?<role=1&offset=0&limit=4>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query params
		query = {
			"role"	 : request.GET.get('role', None),
			"offset" : request.GET.get('offset', None),
			"limit"	 : request.GET.get('limit', None)
		}



		# fetch data
		member_data = fetch_member_data(query)


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
	- /team/interests?<id=1&label=host&member-id=2>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query params
		query = {
			'id'		: request.GET.get('id', None),
			'label'		: request.GET.get('label', None),
			'member-id'	: request.GET.get('member-id', None),
		}

		# fetch data
		interest_data = fetch_interest_data(query)

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

	# fetch member-id
	try:
		if query['member-id'] is not None:
			kwargs['member__id'] = query['member-id']
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
	- /team/roles?<id=1&label=host&member-id=2>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query context
		query = {
			'id'		: request.GET.get('id', None),
			'label'		: request.GET.get('label', None),
			'member-id'	: request.GET.get('member-id', None),
		}

		# fetch data
		role_data = fetch_role_data(query)

		# serialize & return data
		data = serializers.serialize(
										'json', 
										list(role_data), 
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

	# fetch member-id
	try:
		if query['member-id'] is not None:
			kwargs['member__id'] = query['member-id']
	except:
		pass

	# fetch Role data from DB
	roles = Role.objects.filter( **kwargs )


	# return data
	return roles
	
	










