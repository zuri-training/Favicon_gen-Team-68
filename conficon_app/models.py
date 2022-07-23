from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Icon(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/files')
    result = models.ForeignKey('Result', on_delete=models.CASCADE)

class Result(models.Model):
    zip_file = models.FileField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

