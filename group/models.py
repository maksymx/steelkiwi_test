from django.db import models
from student.models import Student

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length = 200)
    chief = models.ForeignKey(Student)
    
    class Meta:
        ordering = ['name']