from django.contrib import admin
from .models import Genre, Movie, Comment, UserLikeMovies, UserDislikeMovie

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(UserLikeMovies)
admin.site.register(UserDislikeMovie)
