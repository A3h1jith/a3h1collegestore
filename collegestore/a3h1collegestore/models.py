from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=250,unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    def __str__(self):
        return self.name