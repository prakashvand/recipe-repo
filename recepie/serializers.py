from rest_framework import serializers
from .models import Category, Recipe, Review
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(recipe=obj)
        if reviews.exists():
            return reviews.aggregate(Avg('rating'))['rating__avg']
        return None

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # recipe = RecipeSerializer() 
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
    
    def get_average_rating(self, obj):
        reviews = Review.objects.filter(recipe=obj.recipe)
        if reviews.exists():
            return reviews.aggregate(Avg('rating'))['rating__avg']
        return None
