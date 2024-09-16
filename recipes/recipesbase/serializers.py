from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length = None, use_url = True)
    recipeCategory = serializers.HyperlinkedRelatedField(
        view_name = 'category_detail',
        queryset = Category.objects.all()
    )

    class Meta:
        model = Recipe
        fields = '__all__'
