from django import forms
from .models import Collectible, Link


class CollectibleModelForm(forms.ModelForm):
    class Meta:
        model = Collectible
        fields = ('collection', 'image', 'name', 'description',
                  'artist', 'publisher','identifier',)


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('name', 'link',)
