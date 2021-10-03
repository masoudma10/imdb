from django.db import models
from users.models import User
from utils.calculate_wilson_mean import confidence
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.name}'




class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    description = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}------\t{self.director}'



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email}\t-----{self.body}\t------{self.rate}'



class UserRatingMovies(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(null=True, blank=True)
    dislike = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.email}\t------{self.movie}'

    @property
    def rating(self):
        return confidence(self.like, self.dislike)

