from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken import views

from core.viewsets import TouristPointViewSet
from resource_tourist.viewsets import ResourceTouristViewSet
from location.viewsets import LocationViewSet
from comment.viewsets import CommentViewSet
from reviews.viewsets import ReviewViewSet


router = routers.DefaultRouter()
router.register(r'pontos-turisticos', TouristPointViewSet, basename='TouristPoint')
router.register(r'recursos-turisticos', ResourceTouristViewSet)
router.register(r'localizacoes', LocationViewSet)
router.register(r'comentarios', CommentViewSet)
router.register(r'avaliacoes', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
