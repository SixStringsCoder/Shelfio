from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.RegexField(label='Nickname', max_length=256, regex=r'^[\w.@+\s]+$')
    image = forms.ImageField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nickname', 'image', 'email',)
        help_texts = {
            'username': ('Letters, digits and @/./+/-/_ only.'),
            'password2': ('Verification.'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Required. 150 characters or fewer.'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter the same password.'}),
        }


class CustomUserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'nickname', 'first_name',
                  'last_name', 'email',)
