from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    profession = models.CharField(max_length=50)
    aadhar_number = models.CharField(max_length=12, blank=True, null=True)
    skills = models.TextField(blank=True)
    is_authenticated = models.BooleanField(default=False)


class Employment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    working_hours = models.FloatField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Attendance(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()


class CashHandover(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
