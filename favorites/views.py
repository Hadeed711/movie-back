from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Favorite
from .serializers import FavoriteSerializer
import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show favorites for the current user
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the current user
        serializer.save(user=self.request.user)

# ✅ New AI Recommendation View
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ai_recommend_view(request):
    prompt = request.data.get("prompt", "")
    if not prompt:
        return Response({"error": "Prompt is required."}, status=400)

    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=100
        )
        recommendation = response.generations[0].text.strip()
        return Response({"recommendation": recommendation})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
