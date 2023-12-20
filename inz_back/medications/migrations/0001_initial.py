# Generated by Django 4.2.7 on 2023-12-05 09:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal_profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('next_dosage_time', models.DateTimeField()),
                ('dosage_interval', models.DurationField(default=datetime.timedelta(days=1))),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='animal_profiles.animal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]