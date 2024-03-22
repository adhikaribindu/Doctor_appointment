from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.


class Doctor(models.Model):
    doctor_name=models.CharField(max_length=25)
    contact=models.IntegerField()
    address=models.TextField(max_length=50)
    specification=models.CharField(max_length=30)
    qualification=models.CharField(max_length=20)
    available_date=models.DateField()
    checkin_time=models.TimeField()
    checkout_time=models.TimeField(blank=True, null=True)


    def __str__(self):
        return self.doctor_name
    
class DoctorDetail(models.Model):
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_fees=models.IntegerField()
    average_rating=models.FloatField()
    experienced_years=models.IntegerField()

    def __str__(self):
        return f"{self.doctor_id.id}"


class DoctorAvailableDate(models.Model):
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    available_day=models.CharField(max_length=50)
    availabletime_slot=models.BinaryField(models.TimeField())    

    
    

