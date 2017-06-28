from django.db import models
from datetime import datetime
from accounts.models import User
from django.utils.text import slugify



    # TODO: add a Priority Field to help user organize a Collection

def collection_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to Collection images

    """
    username = instance.owner.username
    return f"{username}/{instance.name}/{filename}"


def collectible_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to Collectible images

    """
    username = instance.collection.owner.username
    collection = instance.collection.name
    return f"{username}/{collection}/{filename}"


class Category(models.Model):
    """
    Create categories and subcategories

    """
    # TODO: make slugs unique for each collectible entry by user (no duplicates)

    name = models.CharField(max_length=128)
    slug = models.SlugField(editable=False, blank=True, null=False)

    def save(self, *args, **kwargs):
        # auto-save and auto-correct spaces to hyphens
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"  # fixes Admin spelling of Categorys to Categories



class Collection(models.Model):
    """
    Defines a Collection table

    """

    STATUS_CHOICES = (
        ('PRIV', 'Private'),
        ('PUBL', 'Public'),
    )

    owner = models.ForeignKey(User, related_name="collections")
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to=collection_upload_handler, height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=128)
    categories = models.ManyToManyField(Category, related_name='collections')
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, blank=True, null=False)

    def save(self, *args, **kwargs):
        # auto-save if file is new and has no ID yet
        if not self.id:
            self.created = datetime.now()

        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Collectible(models.Model):
    """
    Defines an item or collectible table (within a Collection)

    """

    collection = models.ForeignKey(Collection, related_name="items")
    image = models.ImageField(upload_to=collectible_upload_handler, height_field=None, width_field=None, max_length=200)
    name = models.CharField(max_length=256)
    description = models.TextField()
    creator = models.CharField(max_length=128)
    artist = models.CharField(max_length=128, blank=True, null=True)
    publisher = models.CharField(max_length=128, blank=True, null=True)
    pubyear = models.DateTimeField(blank=True, null=True)
    copyright = models.DateTimeField(blank=True, null=True)
    identifier = models.IntegerField(blank=True, null=True)
    classification = models.ManyToManyField(Category, related_name='collectibles')
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, blank=True, null=False)

    def save(self, *args, **kwargs):
        # auto-save and auto-correct spaces to hyphens
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Link(models.Model):
    """
    Links to media files

    """

    name = models.CharField(max_length=256)
    url = models.URLField(max_length=500)
    collectible = models.ForeignKey(Collectible, related_name="links")
    slug = models.SlugField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
