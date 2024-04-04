from django.db import models
from django.contrib.auth.models import User
from Backend.models import singleDestinationBd

# Create your models here.
# class UserloginDB(models.Model):
#     Email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
#     User = models.CharField(max_length=50, null=True, blank=True)
#     Password = models.CharField(max_length=100, null=True, blank=True)
#
#     def __str__(self):
#         return self.User


class Save_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Date = models.DateField(null=True)
    Quantity = models.IntegerField(default=1)
    single_destination = models.ForeignKey(singleDestinationBd, on_delete=models.CASCADE,null=True,blank=True)
    price = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.Name