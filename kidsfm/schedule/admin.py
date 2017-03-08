from django.contrib 	import admin
from .models 			import Program


# Config admin form for Program model
class ProgramAdmin(admin.ModelAdmin):
    list_display = [
    	'title',
		'description',
		'start_time',
		'end_time',
		'start_date',
		'end_date',
    ]

# Register Program model and admin form
admin.site.register(Program, ProgramAdmin)




