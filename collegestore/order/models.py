from django.db import models

from a3h1collegestore.models import Department, Course

import json

from credentials.models import Material

# Create your models here.

PPS = [
    ('FOR_ENQUIRY' ,'For enquiry'),
    ('PLACE_ORDER','Place order'),
    ('RETURN','Return')
]

GND = [
    ('MALE','Male'),
    ('FEMALE','Female'),
    ('OTHER','Other')
]






class Order(models.Model):
    name = models.CharField(max_length=250)
    DOB = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=25,choices=GND)
    phone_number = models.CharField(max_length=10)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.CharField(max_length=250, choices=PPS)
    materials = models.ManyToManyField(Material)

    def __str__(self):
        return '{}'.format(self.name)


    


