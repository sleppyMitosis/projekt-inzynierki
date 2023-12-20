from rest_framework import serializers
from .models import Medication
from animal_profiles.models import Animal
from animal_profiles.serializers import AnimalSerializer

class MedicationSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Medication
        fields = ['id', 'animal', 'animal_id', 'name', 'start_date', 'end_date', 'dosage_count']

    def create(self, validated_data):
        animal_id = validated_data.pop('animal_id', None)
        medication = Medication.objects.create(**validated_data)
        if animal_id:
            medication.animal = Animal.objects.get(id=animal_id)
            medication.save()
        return medication

    def update(self, instance, validated_data):
        animal_id = validated_data.pop('animal_id', None)
        if animal_id:
            instance.animal = Animal.objects.get(id=animal_id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
