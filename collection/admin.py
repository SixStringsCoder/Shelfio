from django.contrib import admin
from .models import Category, Collection, Collectible, Link

# Register your models here.
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Collectible)
admin.site.register(Link)