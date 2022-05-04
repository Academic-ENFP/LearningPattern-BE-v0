from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField()
    degree = models.IntegerField(null=True, blank=True)
    pf_name = models.CharField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)

class Lecture(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='subject')
    name = models.CharField()
    create_date = models.DateField(auto_now_add=True)
    lecture_time = models.TimeField()
    learning_time = models.TimeField()

class Notes(models.Model):
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='lecture')
    title = models.CharField()
    content = models.CharField()


    

           