from django.conf.urls 		import include, url
from django.contrib 		import admin
#admin.autodiscover()
from django.views.generic 	import TemplateView





urlpatterns = [
    # /
    #
    #    ToDo: 
    #    - make this route specific to the / url
    url(
            r'^$',                  
            TemplateView.as_view(
                template_name='kidsfm/index.html', 
                content_type="text/html"
            ),
            name='index'
    ),





    ########################
    # debug & testing routes
    ########################
    
    # /base
    url(
    		r'^base/',     
            TemplateView.as_view(
                template_name='kidsfm/base.html', 
                content_type="text/html"
            ),
            name='base'
    ),

]






# This enables built-in dev server to serve files from MEDIA_ROOT & STATIC_ROOT
# see: http://stackoverflow.com/a/38446584
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


















