from django.db import models
from users.models import User

#creating patient model
class Patient(models.Model):
    Patient_id=models.AutoField(primary_key=True)
    Patient_name=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient')
    age=models.IntegerField()

    def __str__(self):
        return self.Patient_name