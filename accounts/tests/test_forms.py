import pytest
from mixer.backend.django import mixer
from accounts.forms import CustomUserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile
pytestmark = pytest.mark.django_db


class TestCustomUserCreationForm:
    def test_form_validity(self):
        form = CustomUserCreationForm(data={})
        assert form.is_valid() == False, 'Empty form.  Form must contain data.'

        data = {'email': ''}
        form = CustomUserCreationForm(data=data)
        assert form.is_valid() == False, 'Empty Email Field.  Must contain an email.'

        data = {'nickname': 'Billybob', 'image': 'test.jpg', 'email': 'jr@llama'}
        form = CustomUserCreationForm(data=data)
        assert form.is_valid() == False, 'Email address validator failing.'

        data = {'nickname': 'mamallama', 'image': 'my_image.png', 'email': 'jr@llama.com',
                'password1': 'bobbyyaga', 'password2': 'bobbyyaga'}
        form = CustomUserCreationForm(data=data)
        assert form.is_valid() == False, 'Password validation failed'


        # image_path = 'media/test_image.png'
        # image = SimpleUploadedFile(name='test_image.png', content=open(image_path, 'rb').read(),
        #                            content_type='image/png')
        # data = {'nickname': 'mamallama', 'image': image, 'email': 'jr@llama.com',
        #         'password1': 'bobbyyaga', 'password2': 'bobbyllaba'}
        # form = CustomUserCreationForm(data=data)
        # assert form.is_valid() == False, 'Password validation failed'

