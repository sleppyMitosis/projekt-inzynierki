# models.py

from django.db import models
from animal_profiles.models import Animal

class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='medications', null=True, blank=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    dosage_count = models.IntegerField()

    def __str__(self):
        return self.name
