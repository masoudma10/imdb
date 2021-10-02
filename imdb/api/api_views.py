from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Movie, Comment
from .Exceptions import MovieNotFound, CommentNotFound
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .serializers import CommentSerializer,\
    GenreSerializer,\
    MovieRetrieveSerializer,\
    MovieSerializer



class GenreCreateView(APIView):
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MovieCreateView(APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRetrieveView(APIView):
    def post(self, request):
        serializer = MovieRetrieveSerializer(data=request.data)
        serializer.is_valid()
        valid_data = serializer.validated_data
        name = valid_data.get('name')
        description = valid_data.get('description')
        try:
            movie = Movie.objects.get(name=name)
        except MovieNotFound as e:
            raise ValidationError(e)
        movie_data = MovieSerializer(instance=movie)
        return Response(movie_data.data, status=status.HTTP_200_OK)


class MovieGetSerializer(APIView):
    def get(self, request, genre):
        try:
            movie = Movie.objects.filter(genre__name=genre)
        except MovieNotFound as e:
            raise ValidationError(e)
        serializer = MovieSerializer(instance=movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentShowView(APIView):
    def get(self, request, movie):
        try:
            comment = Comment.objects.filter(movie__name=movie)
        except CommentNotFound as e:
            raise ValidationError(e)
        serializer = CommentSerializer(instance=comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


