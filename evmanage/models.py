from django.db import models

# Create your models here.
class Event(models.Model):
    E_id = models.CharField(max_length=100)
    E_name=models.CharField(max_length=100)
    E_type=models.CharField(max_length=100)
    E_location=models.CharField(max_length=100)
    E_time=models.TimeField()
    E_coordinator_no=models.CharField(max_length=100)
    E_image=models.ImageField(upload_to='pics',default='static/image1.jpg')

    class Meta:
        db_table="Event"

        
class student(models.Model):
    USN = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=30)
    sem = models.IntegerField()
    college = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100,default=0)
    payment_mode = models.CharField(max_length=100,default=0)
    account_no = models.CharField(max_length=100,default=0)
    cvv = models.IntegerField(default=0)
    exp_date = models.DateField(default=2000-12-1)
    E_id = models.ForeignKey(Event,default=-1,on_delete=models.SET_DEFAULT)


    class Meta:
        db_table="student"

        
     


