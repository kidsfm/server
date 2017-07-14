from django.test 	import TestCase
import json


class BlogReSTTestSuite(TestCase):
	fixtures = ['initial_data.json']

	def test_json(self):

		# request json payload
		response = self.client.get('/blog/articles/')

		# test status code
		self.assertEqual(
							response.status_code, 
							200,
							'status code should be 200'
		)

        
		# test json payload
		with open('./blog/fixtures/initial_data.json') as data_file:
			initial_data 	= sorted(json.load(data_file), key=lambda k: k['pk']),
			response_data 	= sorted(response.json(), key=lambda k: k['pk']),


			# is payload the right length
			self.assertEqual( 
								len(response_data[0]),
								len(initial_data[0]),
								'length of response_data doesn\'t match that of initial_data'
			)

			# is payload content as should be
			for i in range( len(response_data[0]) ):
				self.assertEqual( 
									response_data[0][i].get('title'),
									initial_data[0][i].get('title'),
									'title of response_data doesn\'t match that of initial_data'
				)
				#print('\n\tLength of respnse data is: %s\n' % (str(len(response_data[0])),))
				#print('\n\t',i,':\t',response_data[0][i],'\n')







