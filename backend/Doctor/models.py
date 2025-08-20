from django.db import models
from users.models import User


#creating Doctor model
class Doctor(models.Model):
    Doctor_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor')
    Doctor_name=models.CharField(max_length=50)
    Specialization=models.CharField(max_length=50)

    def __str__(self):
        return self.Doctor_name