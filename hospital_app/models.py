from django.db import models


class LOGIN(models.Model):
    
    name1=models.CharField( max_length=100)
    number=models.IntegerField()
    doctor=models.CharField( max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    data=models.DateField()
    
class Search_doctors(models.Model):
    img=models.ImageField( upload_to='photo',)
    name=models.CharField( max_length=50)
    specialization=models.CharField( max_length=50)
    day_in=models.CharField( max_length=50)
    