from django.db import models
from group.models import Group
    
class Student(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 100)
    father = models.CharField(max_length = 100)
    birthday = models.DateField()
    student_card = models.CharField(max_length = 50)
    group_name = models.ForeignKey(Group)
    
    class Meta:
        ordering = ['group_name', 'surname']
