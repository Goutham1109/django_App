from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    title=models.CharField(max_length=20)
    details=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    datacompleted=models.DateTimeField(null=True,blank=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.title