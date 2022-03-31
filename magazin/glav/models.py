from django.db import models

class kamni (models.Model):
    name = models.CharField(max_length=50,blank=False)
    task = models.TextField()
    ss = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name


# Create your models here.
