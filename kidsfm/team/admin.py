from django.contrib import admin
from .forms 		import MemberAdminForm
from .models		import Member, Interests, Role



# Config admin form for Member model
class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm
    prepopulated_fields = {
    	'slug': ('first_name', 'last_name')
    }
    list_display = [
		# ToDo:
		# - enable image preview in Member admin list
		# see: http://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
    	#'profile_img',
    	'first_name',
    	'last_name',
    	'role',
    ]

# Register Member model and admin form
admin.site.register(Member, MemberAdmin)



# Config admin form for Member model
class RoleAdmin(admin.ModelAdmin):
    list_display = [
    	'label',
    	'description',
    ]

# Register Role model and admin form
admin.site.register(Role, RoleAdmin)



# Config admin form for Member model
class InterestsAdmin(admin.ModelAdmin):
    list_display = [
    	'label',
    	'description',
    ]

# Register Interests model and admin form
admin.site.register(Interests, InterestsAdmin)






