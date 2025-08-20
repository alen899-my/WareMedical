from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES=(
        ('admin', 'Admin'),
        ('receptionist', 'Receptionist'),
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('pharmacist', 'Pharmacist'),

    )
    role=models.CharField(max_length=30,choices=ROLES)
    def __str__(self):
        return f"{self.username} ({self.role})"