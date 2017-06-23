from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.RegexField(label=('Nickname'), max_length=256,
                                regex = r'^[\w.@+\s]+$'),

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nickname', 'email')


# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta(UserChangeForm.Meta):
#         model = User
#         fields = UserChangeForm.Meta.fields + ('nickname')