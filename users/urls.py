from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CategoryViewSet, RatingCreateAPIView, ReviewCreateAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('reviews/', ReviewCreateAPIView.as_view()),
    path('ratings/', RatingCreateAPIView.as_view()),
]+router.urls
