from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name