from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from movierater.api.serializers import UserSerializer, FilmSerializer
from movierater.api.models import Film


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
