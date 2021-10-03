from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Movie, Comment, UserLikeMovies, UserDislikeMovie
from .Exceptions import MovieNotFound, CommentNotFound
from ..permissions import UserPermissions
from rest_framework.exceptions import ValidationError
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from ..task import send_email_task
from .serializers import CommentSerializer,\
    GenreSerializer,\
    MovieRetrieveSerializer,\
    MovieSerializer, UserLikeMovies, UserDislikeMovie



class GenreCreateView(APIView):
    """ create genre only
     permissions: admin users """

    permission_classes = [UserPermissions, IsAuthenticated]
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MovieCreateView(APIView):
    """
    create movie api
    """
    permission_classes = [UserPermissions, IsAuthenticated]
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid()
        valid_data = serializer.validated_data
        name = valid_data.get('name')
        description = valid_data.get('description')
        if serializer.is_valid():
            serializer.save()
            send_email_task(name, description)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieUpdateView(APIView):
    """
    update movie
    """
    permission_classes = [UserPermissions, IsAuthenticated]
    def put(self, request, name):
        try:
            movie = Movie.objects.get(name=name)
        except MovieNotFound as e:
            raise ValidationError(e)
        serializer = MovieSerializer(instance=movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRetrieveView(APIView):
    """
    search for movie with name and description
    """

    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = MovieRetrieveSerializer(data=request.data)
        serializer.is_valid()
        valid_data = serializer.validated_data
        name = valid_data.get('name')
        description = valid_data.get('description')
        if name:
            try:
                movie = Movie.objects.get(name=name)
            except MovieNotFound as e:
                raise ValidationError(e)
            movie_data = MovieSerializer(instance=movie)
            return Response(movie_data.data, status=status.HTTP_200_OK)
        elif description:
            try:
                movie = Movie.objects.get(description__icontains=description)
            except MovieNotFound as e:
                raise ValidationError(e)
            movie_data = MovieSerializer(instance=movie)
            return Response(movie_data.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



class MovieGetView(APIView):

    """
    list movie by genre filter
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, genre):
        try:
            movie = Movie.objects.filter(genre__name=genre)
        except MovieNotFound as e:
            raise ValidationError(e)
        serializer = MovieSerializer(instance=movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateView(APIView):

    """add a comment for a movie"""
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentShowView(APIView):
    """
    list comments for a movie
    """

    permission_classes = [IsAuthenticated]
    def get(self, request, movie):
        try:
            comment = Comment.objects.filter(movie__name=movie)
        except CommentNotFound as e:
            raise ValidationError(e)
        serializer = CommentSerializer(instance=comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeCreate(generics.CreateAPIView):
    serializer_class = UserLikeMovies


    def get_queryset(self):
        user = self.request.user
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        return UserLikeMovies.objects.filter(user=user, movie=movie)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('you have already voted for this')
        serializer.save(user=self.request.user, movie=Movie.objects.get(pk=self.kwargs['pk']))


class DislikeCreate(generics.CreateAPIView):
    serializer_class = UserDislikeMovie


    def get_queryset(self):
        user = self.request.user
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        return UserDislikeMovie.objects.filter(user=user, movie=movie)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('you have already voted for this')
        serializer.save(user=self.request.user, movie=Movie.objects.get(pk=self.kwargs['pk']))



