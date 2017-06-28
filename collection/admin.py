from django.contrib import admin
from .models import Category, Collection, Collectible, Link


class LinkInline(admin.StackedInline):
    model = Link


class CollectibleModelAdmin(admin.ModelAdmin):
    model = Collectible
    inlines = [LinkInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Collectible, CollectibleModelAdmin)
admin.site.register(Link)