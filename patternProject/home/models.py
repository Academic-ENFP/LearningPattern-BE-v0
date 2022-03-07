from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    id = models.CharField(max_length=20,primary_key=True)
    pw = models.CharField(max_length=20)
    
    def __str__(self):
        return self.id

class Lecture(models.Model):
    lec_idx = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=20)
    professor = models.CharField(max_length=10)
    student = models.ForeignKey("User", related_name="student", on_delete=models.CASCADE, db_column="student")
    class_time = models.TimeField(auto_now=False, auto_now_add=False)
    learing_time = models.TimeField(auto_now=False, auto_now_add=False)
    completion = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.lec_idx
    
