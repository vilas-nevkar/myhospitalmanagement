# Generated by Django 3.0.1 on 2021-04-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=125)),
                ('doctor_name', models.CharField(max_length=125)),
                ('appointment_date', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=520)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('address', models.CharField(max_length=125)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDischargeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=125)),
                ('doctor_name', models.CharField(max_length=125)),
                ('address', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('symptoms', models.CharField(max_length=250, null=True)),
                ('admit_date', models.DateField()),
                ('release_date', models.DateField()),
                ('doctor_charges', models.PositiveIntegerField()),
                ('room_charges', models.PositiveIntegerField()),
                ('medicine_charges', models.PositiveIntegerField()),
                ('other_charges', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField()),
            ],
        ),
    ]
