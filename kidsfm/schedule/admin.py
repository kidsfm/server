from django.contrib 	import admin
from .models 			import Program, Slot



# Config inline admin form for Slot model
class SlotInline(admin.TabularInline):
	model = Slot
	extra = 1

# Config admin form for Program model
class ProgramAdmin(admin.ModelAdmin):
    list_display = [
    	'title',
		'description',
		#'start_time',
		#'end_time',
		#'start_date',
		#'end_date',
    ]
    inlines = [SlotInline]

# Register Program model and admin form
admin.site.register(Program, ProgramAdmin)




## Config admin form for Slot model
#class SlotAdmin(admin.ModelAdmin):
#    list_display = [
#    	'day',
#		'start_time',
#		'end_time',
#		'start_date',
#		'end_date',
#    ]
#    inlines = [SlotInline]
#
## Register Slot model and admin form
#admin.site.register(Slot, SlotAdmin)




