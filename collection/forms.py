from django import forms
from .models import Collectible, Link, Collection


class CollectionModelForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('status', 'name', 'type',
                  'image', 'categories',)

    def clean_name(self):
        data = self.cleaned_data.get('name')
        if len(data) <= 2:
            raise forms.ValidationError('Form must be invalid. Name must be more than 1 character.')
        if data.isdigit():
            raise forms.ValidationError('Form cannot be all digits.')
        return data


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





