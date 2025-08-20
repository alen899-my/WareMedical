from django.db import models
from users.models import User

#creating Receptionist model
class Receptionist(models.Model):
    Receptionist_id=models.AutoField(primary_key=True)
    Receptionist_name=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='receptionist')