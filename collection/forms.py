from django import forms
from .models import Collectible, Link, Collection


class CollectionModelForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('status', 'name', 'type',
                  'categories',)


class CollectibleModelForm(forms.ModelForm):
    class Meta:
        model = Collectible
        fields = ('collection', 'image', 'name', 'description',
                  'artist', 'publisher', 'identifier',)


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('name', 'link',)
