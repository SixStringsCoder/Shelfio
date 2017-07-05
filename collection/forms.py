from django import forms
from .models import Collectible, Link, Collection


class CollectionModelForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('status', 'name', 'type',
                  'image', 'categories',)


class CollectibleModelForm(forms.ModelForm):
    class Meta:
        model = Collectible
        fields = ('collection', 'image', 'name', 'description',
                  'creator', 'artist', 'publisher', 'identifier',)


class LinkModelForm(forms.ModelForm):
    """
    Form for individual user links

    """

    class Meta:
        model = Link
        fields = ('name', 'url',)
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Type Link Name Here'}),
        #     'url': forms.URLInput(attrs={'placeholder': 'https://www.somelink.com'}),
        # }





