from django.db import models

# Create your models here.

class Profile(models.Model):
    GENDER = (
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Others' , 'Others'),
    )

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Profile/', default='defult/profile.jpg', null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=25, null=True, blank=True)
    Brith_day = models.TextField()
    Gender = models.CharField(max_length=10, choices=GENDER)
    phone_number = models.TextField()
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name



