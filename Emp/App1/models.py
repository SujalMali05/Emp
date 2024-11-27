from django.db import models

# Create your models here.

class Emp(models.Model):
    Emp_name = models.CharField(max_length=20)
    Emp_age = models.IntegerField()
    Salary = models.IntegerField()

    def __str__(self):
        return self.Emp_name

