from django.db import models

# Create your models here.
class contactform(models.Model):
    email = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.email