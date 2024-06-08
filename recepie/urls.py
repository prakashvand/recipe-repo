from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',CategoryList.as_view(), name='category-list'),
    path('recipes/',RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
