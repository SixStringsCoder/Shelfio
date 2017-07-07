from collection import forms


class TestCollectionModelForm:
    def test_form(self):
        form = forms.CollectionModelForm(data={})
        assert form.is_valid() is False, 'No data provided. Form needs to be invalid.'

        data = {'name': 'H'}
        form = forms.CollectionModelForm(data=data)
        assert form.is_valid() is False, 'Form must be invalid.'
        assert 'name' in form.errors, 'Must return form error for name'

        # data = {'name': 1}
        # form = forms.CollectionModelForm(data=data)
        # assert form.is_valid() is False, 'Form must be invalid. Name cannot be a number and must be more than 1 character long'
        #
        #
        # data = {'name': 'Sarah Bellum'}
        # form = forms.CollectionModelForm(data=data)
        # assert form.is_valid() is True, 'Form can only be valid if name is more than 1 character'