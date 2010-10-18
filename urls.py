from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','Projects.views.detail_project',{'project_id':1}),
    (r'^news/(?P<news_id>\d+)/$','Projects.views.detail_news',{'project_id':1}),
    (r'^news/(?P<news_id>\d+)/edit/$','Projects.views.edit_news',{'project_id':1}),
    (r'^news/(?P<news_id>\d+)/delete/$','Projects.views.delete_news',{'project_id':1}),
    
    url(r'^project/(?P<project_id>\d+)/news/add/$','Projects.views.add_news',name='add_news'),
    url(r'^project/(?P<project_id>\d+)/$','Projects.views.detail_project',name='project_main'),
    url(r'^project/(?P<project_id>\d+)/news/(?P<news_id>\d+)/$','Projects.views.detail_news',name='detail_news'),
    url(r'^project/(?P<project_id>\d+)/news/(?P<news_id>\d+)/edit/$','Projects.views.edit_news',name='edit_news'),
    url(r'^project/(?P<project_id>\d+)/news/(?P<news_id>\d+)/delete/$','Projects.views.delete_news',name='delete_news'),
    url(r'^project/(?P<project_id>\d+)/tickets/$','Tickets.views.list_tickets',name='tickets'),
    url(r'^project/(?P<project_id>\d+)/tickets/add/$','Tickets.views.add_ticket',name='add_ticket'),
    url(r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/$','Tickets.views.detail_ticket',name='detail_ticket'),
    url(r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/edit/$','Tickets.views.edit_ticket',name='edit_ticket'),
    url(r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/delete/$','Tickets.views.delete_ticket',name='delete_ticket'),
    url(r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/comment/(?P<comment_id>\d+)/delete/$','Tickets.views.delete_comment',name='delete_comment_in_ticket'),
    url(r'^project/new/','Projects.views.new_project',name='create_project'),
    url(r'^project/(?P<project_id>\d+)/edit/$','Projects.views.edit_project',name='edit_project'),
    url(r'^tag/(?P<tag>\w+)/','Projects.views.list_project_by_tag',name='by_tag'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'media/'}),
#    (r'^account/', include('registration.urls')),
    url(r'^account/register/$','UserProfile.views.register',name='register'),
    url(r'^account/$','UserProfile.views.account',name='account'),
    url(r'^account/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'},name='login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},name='logout'),
    url(r'^account/messages/inbox/$', 'UserProfile.views.messages',{'type':'inbox'},name='inbox'),
    url(r'^account/messages/outbox/$', 'UserProfile.views.messages',{'type':'outbox'},name='outbox'),
    url(r'^account/messages/(?P<message_id>\d+)', 'UserProfile.views.detail_message',name='message'),
    url(r'^account/messages/send/$', 'UserProfile.views.send_message',name='send_message'),
    
#    (r'^','django.views.generic.simple.redirect_to',{'url':'/'})
)