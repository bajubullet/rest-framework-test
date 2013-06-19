from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import permissions
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
  snippets = serializers.PrimaryKeyRelatedField(many=True)
  permission_classes = (permissions.IsAuthenticatedOrReadOnly)

  class Meta:
    model = User
    fields = ('url', 'username', 'snippets')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.Field(source='owner.username')
  highlight = serializers.HyperlinkedIdentityField(
      view_name='snippet-highlight', format='html')

  class Meta:
    model = Snippet
    fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos',
              'language', 'style')
