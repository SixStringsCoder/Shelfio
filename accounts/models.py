from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    User accounts to make collections

    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.

    """
    nickname = models.CharField(max_length=256)

    REQUIRED_FIELDS = ['nickname', 'email']