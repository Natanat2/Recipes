from rest_framework import routers
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewset, basename = 'category')
router.register(r'recipes', views.RecipeViewset, basename = 'recipe')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
