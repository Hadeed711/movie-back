from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet

router = DefaultRouter()
router.register(r'favourites', FavoriteViewSet, basename='favourite')

urlpatterns = [
    path('api/', include(router.urls)),
]