from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=15)
    description=models.CharField(max_length=150)
    image=models.ImageField(upload_to='project/img/')
    url=models.URLField(blank=True)


    def __str__(self):
        return self.title