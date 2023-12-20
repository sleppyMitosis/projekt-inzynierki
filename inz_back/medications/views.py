from rest_framework import viewsets
from .models import Medication
from .serializers import MedicationSerializer  # Import MedicationSerializer here
from rest_framework.permissions import IsAuthenticated

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer  # Use the imported MedicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Custom queryset, e.g., filtering based on the user
        return Medication.objects.filter(animal__owner=self.request.user)

    def perform_create(self, serializer):
        # Any custom save logic when creating a medication
        serializer.save()
