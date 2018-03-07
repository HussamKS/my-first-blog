from django.conf.urls import url
from . import views

urlpatterns = [
#   assigning a view called post_list to the ^$ urls
#   the last part, name = 'post_list' is used to identify the view
    url(r'^$', views.post_list, name ='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
