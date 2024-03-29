from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = patterns('',
  url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
  url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),
      name='snippet-detail'),
  url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
      views.SnippetHighlight.as_view(), name='snippet-highlight'),
  url(r'^users/$', views.UserList.as_view(), name='user-list'),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
  url(r'^$', views.api_root),
)

urlpatterns = format_suffix_patterns(urlpatterns)
