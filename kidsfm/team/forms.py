from django import forms



class MemberForm(forms.Form):
    def clean_interests(self):
	    """
	    Check if there are at most 5 interests
	    """

	    # fetch data that was submitted
	    data = self.cleaned_data['interests']

	    # verify that there aren't more than 5
	    if len(data) > 5:
	        raise forms.ValidationError(
	        						"A member can have at most 5 interests!",
	        						code='invalid'
	        						)

