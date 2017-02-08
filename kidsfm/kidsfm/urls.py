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
    # /*
    url(r'^$', 			TemplateView.as_view(
    											template_name='kidsfm/index.html', 
    											content_type="text/html"
    					),
    					name='index'
    ),

    # /admin/
    url(r'^admin/', 	admin.site.urls),

    # /blog/
    url(r'^blog/', 		include('blog.urls'),		name='blog'),

    # /images/
    url(r'^images/', 	include('images.urls'),		name='images'),

    # /schedule/
    url(r'^schedule/', 	include('schedule.urls'),	name='schedule'),

    # /team/
    url(r'^team/', 		include('team.urls'),		name='team'),

    # /videos/
    url(r'^videos/', 	include('videos.urls'),		name='videos'),




    ########################
    # debug & testing
    ########################
    # /base.html
    url(r'^base/',      TemplateView.as_view(
                                                template_name='kidsfm/base.html', 
                                                content_type="text/html"
                        ),
                        name='base'
    ),


]




