from django.db import models

# Create your models here.
class Profile(models.Model):
        name = models.CharField(max_length = 1200)
        description = models.TextField(default='description default')

def __unicode__(self):
    return self.name
