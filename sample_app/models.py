from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100, default="No Name")
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['name']