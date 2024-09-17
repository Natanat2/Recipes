from rest_framework import routers
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewset, basename = 'category')
router.register(r'recipes', views.RecipeViewset, basename = 'recipe')

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name = 'schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name = 'swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
