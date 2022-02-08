from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed

from movierater.api.serializers import UserSerializer, FilmSerializer, FilmListTitleSerializer
from movierater.api.models import Film


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer

    def get_queryset(self):
        films = Film.objects.all()
        return films

    # dziala automatycznie na ogolny url api np api/films - zwraca liste slownikow
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FilmListTitleSerializer(queryset, many=True)
        return Response(serializer.data)

    # dziala automatycznie na konkretny endpoint(obiekt) np api/films/1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        film = Film.objects.create(title=request.data['title'],
                                   description=request.data['description'],
                                   after_premiere=request.data['after_premiere'])

        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)
        # else:
          #   return HttpResponseNotAllowed('Not Allowed!')

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.title = request.data['title']
        film.description = request.data['description']
        film.after_premiere = request.data['after_premiere']
        film.save()

        serializer = FilmSerializer(film)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        film = self.get_object()
        self.perform_destroy(film)
        return Response(f'Film {film.id} has been deleted')

    # /api/films/3/premiere
    @action(detail=True)  # details mean /3/
    def premiere(self, request, **kwargs):
        film = self.get_object()
        film.after_premiere = True
        film.save()

        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    # /api/films/premiere
    @action(detail=False, methods=['post'])  # for all films in Film model
    def premiere_all(self, request, **kwargs):
        films = Film.objects.all()
        films.update(after_premiere=request.data['after_premiere'])

        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
