from .models import *
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length = None, use_url = True)
    recipeCategory = serializers.HyperlinkedRelatedField(
        view_name = 'category-detail',
        queryset = Category.objects.all()
    )

    class Meta:
        model = Recipe
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    recipes = serializers.HyperlinkedRelatedField(
        many = True,
        view_name = 'recipe-detail',
        read_only = True
    )

    class Meta:
        model = Category
        fields = '__all__'
