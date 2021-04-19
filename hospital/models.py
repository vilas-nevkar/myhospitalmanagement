from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=120)
    mobile = models.CharField(max_length=20, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    address = models.CharField(max_length=125)
    mobile = models.CharField(max_length=20, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=125)
    doctor_name = models.CharField(max_length=125)
    appointment_date = models.DateField(auto_now=True)
    description = models.TextField(max_length=520)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_name


class PatientDischargeDetails(models.Model):
    patient_name = models.CharField(max_length=125)
    doctor_name = models.CharField(max_length=125)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=250, null=True)

    admit_date = models.DateField(null=False)
    release_date = models.DateField(null=False)
    doctor_charges = models.PositiveIntegerField(null=False)
    room_charges = models.PositiveIntegerField(null=False)
    medicine_charges = models.PositiveIntegerField(null=False)
    other_charges = models.PositiveIntegerField(null=False)
    total_amount = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.patient_name
