from django.db import models

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=300, null=True)  # new field for address
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)  # new field for gender
    email = models.EmailField(max_length=100)


    def __str__(self):
        return self.name