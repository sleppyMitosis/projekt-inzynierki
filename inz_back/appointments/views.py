from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer  # Import AppointmentSerializer here
from rest_framework.permissions import IsAuthenticated

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer  # Use the imported AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Custom queryset, e.g., filtering based on the user
        return Appointment.objects.filter(animal__owner=self.request.user)

    def perform_create(self, serializer):
        # Any custom save logic when creating an appointment
        serializer.save()
