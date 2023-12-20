from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Import for permission class
from django.contrib.auth.models import User
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def get_queryset(self):
        """
        This view should return a list of all the animals
        for the currently authenticated user.
        """
        user = self.request.user
        return Animal.objects.filter(owner=user)

    def perform_create(self, serializer):
        """
        Override the default create behavior to associate the animal
        with the current user.
        """
        serializer.save(owner=self.request.user)
