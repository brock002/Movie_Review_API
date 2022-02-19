from django.contrib import admin
from django.apps import apps
from .models import Category, Movie, Review, Rating, CustomUser


# De-register all models from other apps
for app_config in apps.get_app_configs():
    for model in app_config.get_models():
        if admin.site.is_registered(model):
            admin.site.unregister(model)


# Registering only the wanted models
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Rating)
