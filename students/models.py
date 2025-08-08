from django.db import models

class Student(models.Model):
  student_id = models.IntegerField()
  name =  models.CharField(max_length=50)
  branch = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  