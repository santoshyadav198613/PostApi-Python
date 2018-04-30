from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

app_name = 'posts'
urlpatterns = [
    url(r'^posts/$', views.PostsList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostsDetail.as_view(), name='post-detail'),
]
