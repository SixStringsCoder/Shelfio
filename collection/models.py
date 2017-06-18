from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


def image_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to Collection and Collectible images
    :return:
    """
    username = instance.owner.username
    return f"{username}/{filename}"


class Category(models.Model):
    """
    Create categories and subcategories

    """

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Collection(models.Model):
    """
    Describes and defines a Collection

    """

    STATUS_CHOICES = (
        ('PRIV', 'Private'),
        ('PUBL', 'Public'),
    )

    owner = models.ForeignKey(User, related_name="collections")
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to=image_upload_handler, height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=128)
    categories = models.ManyToManyField(Category, related_name='collections')
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # auto-save if file is new and has no ID yet
        if not self.id:
            self.created = datetime.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Collectible(models.Model):
    """
    Describes and defines an item or collectible within a Collection

    """

    collection = models.ForeignKey(Collection, related_name="items")
    image = models.ImageField(upload_to=image_upload_handler, height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=256)
    description = models.TextField()
    creator = models.CharField(max_length=128)
    artist = models.CharField(max_length=128, blank=True, null=True)
    publisher = models.CharField(max_length=128, blank=True, null=True)
    pubyear = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    copyright = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    identifier = models.IntegerField(blank=True, null=True)
    classification = models.ManyToManyField(Category, related_name='collectibles')
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)


class Link(models.Model):
    """
    Links to media files

    """

    name = models.CharField(max_length=256)
    link = models.FileField(null=True, blank=True)
    collectible = models.ForeignKey(Collectible, related_name="links")