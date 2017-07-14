from django.contrib 	import admin
from .models 			import Article




# Config admin form for Article model
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
    	'title',
		'content',
		'author',
    ]

# Register Article model and admin form
admin.site.register(Article, ArticleAdmin)




