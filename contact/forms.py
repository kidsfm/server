from django import forms


class MessageForm(forms.Form):
	"""
	This form enables client to post messages from the contact page.

	URL: 	/contact/
	"""
	name 	= forms.CharField(
					required=True,
					widget=forms.TextInput(
						attrs={
						'class': 'nicdark_bg_grey2 nicdark_radius nicdark_shadow grey small subtitle',
						'placeholder': 'Name'
						}
					),
					max_length=100
	)

	email 	= forms.CharField(
					required=True,
					widget=forms.EmailInput(
						attrs={
						'class': 'nicdark_bg_grey2 nicdark_radius nicdark_shadow grey small subtitle',
						'placeholder': 'Email'
						}
					),
					max_length=50
	)

	message = forms.CharField(
					widget=forms.Textarea(
						attrs={
							'rows': 7, 
							'class': "nicdark_bg_grey2 nicdark_radius nicdark_shadow grey small subtitle",
							'placeholder': 'Message'
						}
					),
					max_length=255
	)




