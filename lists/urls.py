from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^add$',views.add_item, name = 'add_item'),
    url(r'^edit$', views.edit_item_list, name='edit_item_list'),
    url(r'^delete$', views.delete_item_list, name='delete_item_list'),
    url(r'^(?P<pk>[0-9]+)/view/$', views.view_list, name='view_list'),
]
