from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.email
