from django.db import models
from subject.models import Lecture

# Create your models here.

class Analysis(models.Model):
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='lecture')
    concentration_rate = models.FloatField()
    review_section = models.CharField()

class Interaction(models.Model):
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name='lecture')
    interaction_type = models.CharField()
    interaction_time_real = models.TimeField()
    interaction_time_lecture = models.TimeField()