from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url('^post/(?P<post_id>\d+)/$', views.post_comments, name='post_comments'),
]
