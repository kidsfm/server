from django.contrib import admin
from django 		import forms
from .models		import Member, Interests



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
	    # Debug
	    #print('user[%s] has %s interests' % (self.first_name, self.interests.count()) )
	    # verify that there aren't more than 5
	    if data.count() > 5:
	        raise forms.ValidationError(
	        						"A member can have at most 5 interests!",
	        						code='invalid'
	        						)
	    # else return data
	    return data


class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm


admin.site.register(Member, MemberAdmin)




#class InterestsInline(admin.StackedInline):
#    """
#    Allows Interests to be added when creating a Member object in Team app
#    """
#    model = Interests
#    extra = 1
#    max_num = 5
#    min_num = 1 # new in Django 1.7
#
#
#class MemberAdmin(admin.ModelAdmin):
#    inlines = [InterestsInline,]
#
#
#
#
#admin.site.register(Member, MemberAdmin)


