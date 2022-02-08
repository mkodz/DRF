from django.contrib.auth.models import User
from rest_framework import serializers
from movierater.api.models import Film


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'after_premiere']


class FilmListTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title')
