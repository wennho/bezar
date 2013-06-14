from django.db import models

# Create your models here.
class Ad(models.Model):
    create_date    = models.DateField()
    owner = models.ForeignKey(User)
    text = models.TextField()
    