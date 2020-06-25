from django.db import models
from datetime import date

# Create your models here.
class Blogs(models.Model):
    blogtitle=models.CharField(max_length=15)
    description=models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.blogtitle