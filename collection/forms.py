from django import forms
from .models import Collectible, Link, Collection
from django.forms.formsets import formset_factory
# LinkModelFormSet = formset_factory(LinkModelForm)


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
    class Meta:
        model = Link
        fields = ('name', 'link',)



# class LinkModelForm(forms.ModelForm):
#     """
#     Form for collectible links
#
#     """
#     anchor = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Link Name',
#         }),
#         required=False)
#     url = forms.URLField(
#         widget=forms.URLInput(attrs={
#             'placeholder': 'URL',
#         }),
#         required=False)