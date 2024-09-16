from rest_framework import routers
from django.urls import path, include
from recipes.recipesbase import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewset)
router.register(r'recipes', views.RecipeViewset)

urlpatterns = [
    path('api/', include(router.urls))
]
