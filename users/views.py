from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializers import MovieSerializer, CatgeorySerializer, CategoryDetailsSerializer, RatingSerializer, ReviewSerializer
from .models import Movie, Category
from django.db.models import Avg


# get requests for category model
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailsSerializer
        return CatgeorySerializer

# get requests for movie model
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.annotate(rating=Avg('ratings__Count'))
    serializer_class = MovieSerializer

# post request handler for review creation
class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer

# post request handler for rating creation
class RatingCreateAPIView(CreateAPIView):
    serializer_class = RatingSerializer
