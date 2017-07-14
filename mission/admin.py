from django.contrib 	import admin
from .models 			import Statement


# Config admin form for Member model
class StatementAdmin(admin.ModelAdmin):
    list_display = [
    	'title',
    	'description',
    ]

# Register Statement model and admin form
admin.site.register(Statement, StatementAdmin)




