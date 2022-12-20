from django.db import models

# Create your models here.

class commonName(models.Model):
    name = models.CharField(max_length=250,blank=False,default='')
    class Meta:
        abstract = True

class Teacher(commonName):
    department = models.CharField(max_length=250)
    salary = models.IntegerField(blank=False, default=0)

class Students(commonName):
    rollno = models.IntegerField(blank=False,default=0)
    standard = models.CharField(max_length=150,blank=False, default='')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


