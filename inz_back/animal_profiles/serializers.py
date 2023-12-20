# In your animal_profiles/serializers.py

from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = ['id', 'name', 'species', 'date_of_birth']
