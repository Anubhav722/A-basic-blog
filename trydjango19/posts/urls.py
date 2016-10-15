from django.conf.urls import patterns, include, url
from . import views

# urlpatterns=patterns('',
#     url(r'^$', views.list2, name='home'),
# )

urlpatterns=patterns('',
    url(r'^$', views.post_list, name='home'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
    
    
    
    
    #url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    #url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    #url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete'),
)