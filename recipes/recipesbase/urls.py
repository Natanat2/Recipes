from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewset)
router.register(r'recipes', views.RecipeViewset)

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls)),
]
