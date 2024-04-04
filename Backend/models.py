from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DestinationDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="image", null=True, blank=True)

    def __str__(self):
        return self.Name

class PlaceDB(models.Model):
    modeName = models.ForeignKey(DestinationDB,on_delete=models.CASCADE,null=True,blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    P_Price = models.IntegerField(null=True, blank=True)
    P_Description = models.CharField(max_length=1000, null=True, blank=True)
    P_Image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.state




class singleDestinationBd(models.Model):
    modeName = models.ForeignKey(DestinationDB,on_delete=models.CASCADE,null=True, blank=True)
    state = models.ForeignKey(PlaceDB,on_delete=models.CASCADE,null=True, blank=True)
    PlaceName = models.CharField(max_length=100, null=True, blank=True)
    From_To = models.CharField(max_length=1000, null=True, blank=True)
    Duration = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Place_image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.PlaceName

class Hotels(models.Model):
    destination = models.ForeignKey(singleDestinationBd,on_delete=models.CASCADE)
    Hotel_Name = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Hotel_Description = models.CharField(max_length=1000, null=True, blank=True)
    Hotel_image = models.ImageField(upload_to="images", null=True, blank=True)
    def __str__(self):
        return self.Hotel_Name


class Restaurants(models.Model):
    destination = models.ForeignKey(singleDestinationBd,on_delete=models.CASCADE)
    Restaurants_Name = models.CharField(max_length=50, null=True, blank=True)
    Restaurants_Description = models.CharField(max_length=1000, null=True, blank=True)
    Restaurants_image = models.ImageField(upload_to="images", null=True, blank=True)
    def __str__(self):
        return self.Restaurants_Name


class FlightBookingDb(models.Model):
    destination = models.ForeignKey(singleDestinationBd,on_delete=models.CASCADE,null=True)
    Flight_Name = models.CharField(max_length=50, null=True, blank=True)
    From = models.CharField(max_length=50, null=True, blank=True)
    To = models.CharField(max_length=50, null=True, blank=True)
    Depart = models.CharField(max_length=50, null=True, blank=True)
    Arrive = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Flight_Image = models.ImageField(upload_to="image", null=True, blank=True)

    def __str__(self):
        return self.Flight_Name



class Cart(models.Model):
    destination = models.ForeignKey(singleDestinationBd, on_delete=models.CASCADE, null=True)
    Hotel_price = models.IntegerField(null=True, blank=True)
    Total_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Hotel_price


