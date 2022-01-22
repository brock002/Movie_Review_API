from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import MovieSerializer, CatgeorySerializer, RatingSerializer, ReviewSerializer
from .models import Movie, Category
from django.db.models import Avg


# get requests for category model
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatgeorySerializer

# get requests for movie model
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.annotate(rating=Avg('ratings__Count')).order_by('-rating')
    serializer_class = MovieSerializer

# post request handler for review creation
class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer

# post request handler for rating creation
class RatingCreateAPIView(CreateAPIView):
    serializer_class = RatingSerializer

# categories/<id>/movies
class MoviesInCategoryListAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Category.objects.get(id=self.request.path.split('/')[-3]).movies.annotate(rating=Avg('ratings__Count')).order_by('-rating')
