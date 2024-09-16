from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, RecipeSerializer
from .models import Category, Recipe


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


def index(request):
    return render(request, 'index.html')
