from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Form(models.Model):
    Name=CharField(max_length=120)
    Last_Name=CharField(max_length=8)
    Email_id=CharField(max_length=50)

    def __str__(self):
        return self.Name + " "+self.Last_Name
class web(models.Model):
    img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    title=models.CharField(max_length=12)
    description=models.CharField(max_length=50)
    rate=models.IntegerField(max_length=20)

    def __str__(self):
        return self.title

class graphic(models.Model):
    img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    title=models.CharField(max_length=12)
    description=models.CharField(max_length=50)
    rate=models.IntegerField(max_length=20)

    def __str__(self):
        return self.title

class digi(models.Model):
    img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    title=models.CharField(max_length=12)
    description=models.CharField(max_length=50)
    rate=models.IntegerField(max_length=20)

    def __str__(self):
        return self.title