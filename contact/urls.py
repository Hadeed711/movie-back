from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

# We're not going to use this router since the main urls.py already has it
# This is to avoid conflicts between the two routers
urlpatterns = [
    # Empty - the main urls.py will handle contact routes
]