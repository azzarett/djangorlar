from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # дополнительные поля — пример
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
