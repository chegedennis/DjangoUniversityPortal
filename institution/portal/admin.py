from django.contrib import admin
from .models import Constituency, County, Student,Gender,MaritalStatus,Nationality,Relationship,Religion,Dependant,EmergencyContact, SubCounty

# Register your models here.
models = [Constituency,County,SubCounty,Student,Gender,MaritalStatus,Nationality,Religion,Relationship,Dependant,EmergencyContact]
admin.site.register(models)


