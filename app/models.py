from django.db import models
import datetime
# Create your models here.
class Hero_Section(models.Model):
     text= models.CharField(max_length=100)
     text_subtitle= models.CharField(max_length=500)
     img_mobile = models.ImageField(("/mobile"))
     img_web = models.ImageField(("/web"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.text

class Gallery(models.Model):
     name= models.CharField(max_length=500)
     img = models.ImageField(("/gallery"))

     def __str__(self):
         return self.name
         

class Notification(models.Model):
     name= models.CharField(max_length=100)
     content = models.CharField(max_length=500)
     date = models.DateField(default=datetime.date.today , blank=True)
     img = models.ImageField(("/profile"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.name


class Community(models.Model):
     text= models.CharField(max_length=250)
     category = models.CharField(max_length=100)
     img = models.ImageField(("/profile"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.text

class International(models.Model):
     text= models.CharField(max_length=250)
     category = models.CharField(max_length=100)
     img = models.ImageField(("/profile"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.text

class Club(models.Model):
     text= models.CharField(max_length=250)
     category = models.CharField(max_length=100)
     img = models.ImageField(("/profile"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.text

class Vocational(models.Model):
     text= models.CharField(max_length=250)
     category = models.CharField(max_length=100)
     img = models.ImageField(("/profile"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.text

class Professional(models.Model):
     text= models.CharField(max_length=250)
     category = models.CharField(max_length=100)
     img = models.ImageField(("/profile"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.text

class Council(models.Model):
     position= models.CharField(max_length=250)
     name = models.CharField(max_length=100)
     img = models.ImageField(("/council"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.name

class Director(models.Model):
     position= models.CharField(max_length=250)
     name = models.CharField(max_length=100)
     rotaryid = models.CharField(max_length=100)
     img = models.ImageField(("/council"))
     url = models.URLField(max_length=200)

     def __str__(self):
         return self.name