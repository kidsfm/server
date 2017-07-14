from django.conf.urls 		import include, url
from django.contrib 		import admin
#admin.autodiscover()
from django.views.generic 	import TemplateView





urlpatterns = [
    url(
        r'^$',                  
        TemplateView.as_view(
            template_name='kidsfm/index.html', 
            content_type="text/html"
        ),
        name='index'
    ),

    # /*
    #
    #    ToDo: 
    #    - use this route to handle 404 errors
    #url(r'^$',                  TemplateView.as_view(
    #                                            template_name='kidsfm/404.html', 
    #                                            content_type="text/html"
    #                            ),
    #                            name='404'
    #),

    # /listen
    #
    #    ToDo: 
    #    - implement the listen route
    #url(r'^listen/$',            TemplateView.as_view(
    #                                            template_name='kidsfm/listen.html', 
    #                                            content_type="text/html"
    #                            ),
    #                            name='listen'
    #),

    # /media
    #
    #    ToDo: 
    #    - implement the media route
    #url(r'^media/$',            TemplateView.as_view(
    #                                            template_name='kidsfm/media.html', 
    #                                            content_type="text/html"
    #                            ),
    #                            name='media'
    #),





    ########################
    # App routes
    ########################
    
    # /admin/
    url(
        r'^admin/',     
        admin.site.urls
    ),

    # /blog/
    url(
        r'^blog/',      
        include('blog.urls'),       
        name='blog'
    ),

    # /contact
    url(
        r'^contact/',   
        include('contact.urls'),    
        name='contact'
    ),

    # /images/
    url(
        r'^images/',    
        include('images.urls'),     
        name='images'
    ),

    # /mission/
    url(
        r'^mission/',   
        include('mission.urls'),    
        name='mission'
    ),

    # /oauth2/
    url(
        r'^oauth2/',    
        include('oauth2.urls'),     
        name='oauth2'
    ),

    # /schedule/
    url(
        r'^schedule/',  
        include('schedule.urls'),   
        name='schedule'
    ),

    # /team/
    url(
        r'^team/',      
        include('team.urls'),       
        name='team'
    ),

    # /theme/
    url(
        r'^theme/',     
        include('theme.urls'),      
        name='theme'
    ),

    # /videos/
    url(
        r'^videos/',    
        include('videos.urls'),    
         name='videos'
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


















