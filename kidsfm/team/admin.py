from django.contrib import admin
from .models		import Member, Interests



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

admin.site.register(Member)
