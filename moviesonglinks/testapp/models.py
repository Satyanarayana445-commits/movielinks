from django.db import models
class Movie(models.Model):
    name=models.CharField(max_length=100);
    link=models.URLField(("link"),max_length=128,db_index=True,unique=True,blank=True)
