from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','the_project.Projects.views.detail_project',{'project_id':1}),
    (r'^news/(?P<news_id>\d+)/$','the_project.Projects.views.detail_news',{'project_id':1}),
    (r'^users/(?P<user_id>\d+)/$','the_project.views.detail_user'),
    
    (r'^project/(?P<project_id>\d+)/news/add/$','the_project.Projects.views.add_news'),
    (r'^project/(?P<project_id>\d+)/$','the_project.Projects.views.detail_project'),
    (r'^project/(?P<project_id>\d+)/news/(?P<news_id>\d+)/$','the_project.Projects.views.detail_news'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/mik/Aptana Studio 3 Workspace/the_project/src/the_project/media/'}),
)