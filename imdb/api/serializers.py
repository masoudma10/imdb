from rest_framework import serializers
from ..models import Genre, Movie, Comment,UserLikeMovies, UserDislikeMovie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = '__all__'


class MovieRetrieveSerializer(serializers.Serializer):
    description = serializers.CharField(required=False)
    name = serializers.CharField(required=False)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLikeMovies
        fields = '__all__'


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDislikeMovie
        fields = '__all__'

