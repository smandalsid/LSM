from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    regno=models.CharField(max_length=9, null=False, blank=False)
    trips=models.IntegerField(null=False, blank=False)
    balance=models.BigIntegerField(null=False, blank=False)
    def __str__(self):
        return self.regno
    
class Images(models.Model):
    # imguser=models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False)
    imgid=models.IntegerField(primary_key=True, null=False, blank=False)
    img=models.ImageField(null=False, blank=False)

    def __str__(self):
        return str(self.imgid)