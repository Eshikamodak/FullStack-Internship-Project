from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(default="")
    username = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")

    def _str_(self):
        return self.username
    