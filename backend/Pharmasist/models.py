from django.db import models
from users.models import User

#creating Pharmasist model

class Pharmasist(models.Model):
    pharmasist_id=models.AutoField(primary_key=True)
    pharmasist_name=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='pharmasist')

    def __str__(self):
        return self.pharmasist_name