from django.contrib import admin
from .forms 		import MemberAdminForm
from .models		import Member


# Config admin form for Member model
class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm


# Register Member model and admin form
admin.site.register(Member, MemberAdmin)






