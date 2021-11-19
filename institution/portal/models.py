from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class MaritalStatus(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Nationality(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Religion(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class SubCounty(models.Model):
    name = models.CharField(max_length=60)
    county = models.ForeignKey(County,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Constituency(models.Model):
    name = models.CharField(max_length=60)
    subcounty = models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.SET_NULL)
    regno = models.CharField(max_length=50, blank=True,null=True)
    maritalstatus = models.ForeignKey(MaritalStatus,null=True,on_delete=models.SET_NULL)
    disability = models.CharField(max_length=50, blank=True,null=True)
    nationalid = models.IntegerField(blank=True,null=True)
    dob = models.DateField(null=True,blank=True)
    phone = models.IntegerField(blank=True,null=True)
    nationality =  models.ForeignKey(Nationality,null=True,on_delete=models.SET_NULL)
    religion =  models.ForeignKey(Religion,null=True,on_delete=models.SET_NULL)
    homeaddress = models.CharField(max_length=50, blank=True,null=True)
    county =  models.ForeignKey(County,null=True,on_delete=models.SET_NULL)
    subcounty =  models.ForeignKey(SubCounty,null=True,on_delete=models.SET_NULL)
    constituency =  models.ForeignKey(Constituency,null=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.name.username


class Relationship(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EmergencyContact(models.Model):
    firstname = models.CharField(max_length=50, null=True,blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    relationship = models.OneToOneField(Relationship, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.firstname
    
class Dependant(models.Model):
    firstname = models.CharField(max_length=50, null=True,blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    relationship = models.OneToOneField(Relationship, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    occupation = models.CharField(max_length=100,blank=True,null=True)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.firstname
