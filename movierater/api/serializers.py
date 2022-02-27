from django.contrib.auth.models import User
from rest_framework import serializers
from movierater.api.models import Film, ExtraInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ('time', 'kind')


class FilmSerializer(serializers.ModelSerializer):
    extra = ExtraInfoSerializer(many=False)
    class Meta:
        model = Film
        fields = ('id', 'title', 'description', 'after_premiere',
                  'premiere', 'year', 'imdb_rating', 'extra')


# class FilmListTitleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Film
#         fields = ('id', 'title')
