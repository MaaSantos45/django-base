from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)

    def __str__(self):
        return self.author.get_full_name() or self.author.username
