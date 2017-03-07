from django.contrib 	import admin
from .models 			import Message


# Config admin form for Member model
class MessageAdmin(admin.ModelAdmin):
    list_display = [
    	'name',
    	'email',
    	'message',
    ]

# Register Message model and admin form
admin.site.register(Message, MessageAdmin)




