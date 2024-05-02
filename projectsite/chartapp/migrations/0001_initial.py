# Generated by Django 5.0.4 on 2024-05-02 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firefighters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('rank', models.CharField(max_length=150)),
                ('experience_level', models.CharField(max_length=150)),
                ('station', models.CharField(blank=True, choices=[('Probationary Firefighter', 'Probationary Firefighter'), ('Firefighter I', 'Firefighter I'), ('Firefighter II', 'Firefighter II'), ('Firefighter III', 'Firefighter III'), ('Driver', 'Driver'), ('Captain', 'Captain'), ('Battalion Chief', 'Battalion Chief')], max_length=45, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FireStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FireTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('truck_number', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('capacity', models.CharField(max_length=150)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chartapp.firestation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('severity_level', models.CharField(choices=[('Minor Fire', 'Minor Fire'), ('Moderate Fire', 'Moderate Fire'), ('Major Fire', 'Major Fire')], max_length=45)),
                ('description', models.CharField(max_length=250)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chartapp.locations')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=10)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weather_description', models.CharField(max_length=150)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chartapp.incident')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
