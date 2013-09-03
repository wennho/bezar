from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ad(models.Model):
    title = models.CharField(max_length=140)
    create_datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.CharField(max_length=140)
    owner = models.ForeignKey(User)
    description = models.TextField()

    def __unicode__(self):
        return self.title

class ScrapedAd(models.Model):
    title = models.CharField(max_length=140)
    create_datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.CharField(max_length=140)
    url = models.CharField(max_length=140)

    def __unicode__(self):
        return self.title
