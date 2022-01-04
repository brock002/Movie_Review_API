from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email.split('@')[0]


class Category(models.Model):
    NAME = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.NAME


class Movie(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['cover_pic', str(instance.NAME), filename])

    NAME = models.TextField(blank=False)
    COVER = models.ImageField(upload_to=nameFile, blank=True)
    CATEGORIES = models.ManyToManyField(Category, related_name='movies')
    CAST = models.TextField(blank=False)
    DESCRIPTION = models.TextField(blank=False)

    def __str__(self):
        return self.NAME


class Review(models.Model):
    Review = models.TextField()
    MOVIE = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    USER = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    # LIKES = models.IntegerField()
    # DISLIKES = models.IntegerField()

    def __str__(self):
        return self.Review


class Rating(models.Model):
    Count = models.IntegerField()
    MOVIE = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    USER = models.ForeignKey(CustomUser, related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Count)
