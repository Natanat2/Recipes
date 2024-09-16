from django.shortcuts import render

from rest_framework import viewsets

from recipes.recipesbase.serializers import *
from recipes.recipesbase.models import *


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
