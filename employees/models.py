from django.db import models
from .string import GENDER_CHOICES

# Create your models here.
class Employee(models.Model):
    emp_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Select')
    designation = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=10)
    district = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name+'-'+self.last_name



