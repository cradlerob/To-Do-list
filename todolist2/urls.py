from django.conf.urls import include, url
from django.contrib import admin
from lists import urls as lists_urls
from lists import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'todolist2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/', include(lists_urls)),
]
