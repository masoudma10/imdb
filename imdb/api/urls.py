from django.urls import path
from . import api_views

app_name = 'imdb'


urlpatterns = [
    path('genre_create/', api_views.GenreCreateView.as_view(), name='genre_create'),
    path('movie_create/', api_views.MovieCreateView.as_view(), name='movie_create'),
    path('movie_retrieve/', api_views.MovieRetrieveView.as_view(), name='movie_retrieve'),
    path('movie_get/<str:genre>/', api_views.MovieGetView.as_view(), name='movie_get'),
    path('movie_update/<str:name>/', api_views.MovieUpdateView.as_view(), name='movie_update'),
    path('comment_create/', api_views.CommentCreateView.as_view(), name='comment_create'),
    path('comment_show/<str:movie>/', api_views.CommentShowView.as_view(), name='comment_show'),
    path('like/<int:pk>/', api_views.LikeCreate.as_view(), ),
    path('dislike/<int:pk>/', api_views.DislikeCreate.as_view(), ),
]