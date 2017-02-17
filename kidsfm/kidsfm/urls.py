"""kidsfm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls 		import include, url
from django.contrib 		import admin
from django.views.generic 	import TemplateView



urlpatterns = [

    ########################
    # Pages routes
    ########################

    # /
    #
    #    ToDo: 
    #    - make this route specific to the / url
    url(r'^$',                  TemplateView.as_view(
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

    # /contact
    url(r'^contact/$',          TemplateView.as_view(
                                                template_name='kidsfm/contact.html', 
                                                content_type="text/html"
                                ),
                                name='contact'
    ),

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

    # /mission
    url(r'^mission/$',          TemplateView.as_view(
                                                template_name='kidsfm/mission_statements.html', 
                                                content_type="text/html"
                                ),
                                name='mission_statements'
    ),

    # /mission/<mission-slug>
    url(r'^mission/(?P<mission_slug>[\w\-]+)/$',    TemplateView.as_view(
                                                template_name='kidsfm/mission_single.html', 
                                                content_type="text/html"
                                ),
                                name='mission_single'
    ),





    ########################
    # App routes
    ########################
    
    # /admin/
    url(r'^admin/', 	admin.site.urls),

    # /blog/
    url(r'^blog/', 	    include('blog.urls'),		name='blog'),

    # /images/
    url(r'^images/', 	include('images.urls'),		name='images'),

    # /oauth2/
    url(r'^oauth2/',    include('oauth2.urls'),     name='oauth2'),

    # /schedule/
    url(r'^schedule/',  include('schedule.urls'),	name='schedule'),

    # /team/
    url(r'^team/',      include('team.urls'),		name='team'),

    # /videos/
    url(r'^videos/', 	include('videos.urls'),		name='videos'),





    ########################
    # debug & testing routes
    ########################
    
    # /base
    url(r'^base/',     TemplateView.as_view(
                                                template_name='kidsfm/base.html', 
                                                content_type="text/html"
                        ),
                        name='base'
    ),


]





