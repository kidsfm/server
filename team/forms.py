from django 	import forms
from .models	import Member



# Config validation for admin form for Member model
class MemberAdminForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = '__all__'

	def clean_interests(self):
	    """
	    Check if there are at most 5 interests
	    """
	    # fetch data that was submitted
	    data = self.cleaned_data['interests']
	    # verify that there aren't more than 5
	    if data.count() > 5:
	        raise forms.ValidationError(
	        						"A member can have at most 5 interests!",
	        						code='invalid'
	        						)
	    # else return data
	    return data


