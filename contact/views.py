from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]  # Explicitly allow anyone to send messages

    def get_queryset(self):
        """
        Only show contacts to admin users in list view.
        For non-admin users creating contacts, we still allow creation.
        """
        if self.request.user.is_staff:
            return Contact.objects.all()
        return Contact.objects.none()