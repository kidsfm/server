from django.contrib 	import admin
from .models 			import Message, Location


# Config admin form for Message model
class MessageAdmin(admin.ModelAdmin):
    list_display = [
    	'name',
    	'email',
    	'message',
    ]

# Register Message model and admin form
admin.site.register(Message, MessageAdmin)


# Config admin form for Member model
class LocationAdmin(admin.ModelAdmin):
    list_display = [
    	'title',
    	'address',
    	'city',
    	'state',
    	'country',
    ]

# Register Location model and admin form
admin.site.register(Location, LocationAdmin)




