"""
URL configuration for movie_search project.
"""
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from favorites.views import FavoriteViewSet
from contact.views import ContactViewSet

router = DefaultRouter()
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ✅ Fixed: Add both regular djoser urls and JWT urls
    path('auth/', include('djoser.urls')),           # This gives us /auth/users/
    path('auth/', include('djoser.urls.jwt')),       # This gives us /auth/jwt/create/, /auth/jwt/refresh/, etc.
    
    # ✅ Keep your custom user URLs if needed
    path('api/auth/', include('users.urls')),
    
    # ✅ Alternative JWT endpoints (you can keep these as backup)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include router urls
    path('api/', include(router.urls)),
    path('api/', include('favorites.urls')),
]