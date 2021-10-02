from django.db import models
from users.models import User

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
    rate = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.name}------\t{self.director}'


    def rating_calculate(self):
        pass



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    rate = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email}\t-----{self.body}\t------{self.rate}'


