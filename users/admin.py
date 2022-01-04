from django.contrib import admin

from .models import Category, Movie, Review, Rating, CustomUser

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Rating)
