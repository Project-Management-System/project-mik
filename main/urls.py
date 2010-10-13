from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

demo = {
        'menu':['Menu 1','Menu 2','Menu 3','Menu 4','Menu 5'],
        }

urlpatterns = patterns('',
    # Example:
    # (r'^the_project/', include('the_project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$','django.views.generic.simple.direct_to_template',{'template':'placeholder.html'}),
    (r'^demo/$',include('the_project.main.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/media/'}),
)