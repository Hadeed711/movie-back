from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet, ai_recommend_view  

router = DefaultRouter()
router.register(r'favourites', FavoriteViewSet, basename='favourite')

urlpatterns = [
    path('api/', include(router.urls)),
    path('/recommend/', ai_recommend_view),  
]
