from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to User profile image

    """
    username = instance.username
    return f"{username}/avatar/{filename}"


class User(AbstractUser):
    """
    User accounts to make collections

    Users within the Django authentication system are represented by this
    model.

    Username, image and email are required. Other fields are optional.

    """
    nickname = models.CharField(max_length=256)
    image = models.ImageField(upload_to=profile_upload_handler, null=True, blank=True)

    REQUIRED_FIELDS = ['nickname', 'email', ]
