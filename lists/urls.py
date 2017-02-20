from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^$', views.new_list, name='new_list'),
    url(r'^(?P<pk>[0-9]+)/add$',views.add_item, name = 'add_item'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.edit_item_list, name='edit_item'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.delete_item_list, name='delete_item'),
    url(r'^(?P<pk>[0-9]+)/view/$', views.view_list, name='view_list'),
url(r'^(?P<pk>[0-9]+)/delete_list/$', views.delete_list, name='delete_list'),
]
