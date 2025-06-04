from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import UserCreateSerializer, UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserSerializer  # Or create a custom token serializer if needed

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    authentication_classes = []
    permission_classes = []