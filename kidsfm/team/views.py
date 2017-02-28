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

	URL: 	/team/members?<q1=arg1&q2=arg2>

	ToDo:
	- validate query & send "bad format" status code if invalid
	'''
	def get(self, request):

		# fetch query params
		q_dict = dict()
		q_dict['role'] 		= request.GET.get('role', None)
		q_dict['offset'] 	= request.GET.get('offset', None)
		q_dict['limit'] 	= request.GET.get('limit', None)

		# Debug
		#print('\tNow in team.views.Members_json.get')
		#print('\tquery is: %s' % (q_dict,))

		
		# fetch data
		members = fetch_member_data(q_dict)

		# serialize & return data
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
	- join Interests & Role models in DB lookup

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
	

	# fetch data from DB
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



	# return results
	return members
	
	










