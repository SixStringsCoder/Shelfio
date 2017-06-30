from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth .forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required



def login(request):
    """
    Login rules and redirect

    """

    if request.method == 'GET':
        form = AuthenticationForm()
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)

            if user is not None:
                django_login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, f'You do not have an account. Please register.')

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def register(request):
    """
    Registration rules and redirects

    """

    if request.method == 'GET':
        form = CustomUserCreationForm()

    elif request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Add non-required additions to instance if needed
            user.save()

            send_mail(
                subject='You have a Shelfio account!',
                message='Sign in and get organized!  Share your Collections with friends!',
                from_email='rshanlon3@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)

            return redirect('/') # TODO: success redirect to some web page

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required()
def profile(request):
    """
    Update user profile information

    """

    form = CustomUserUpdateForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)

    context = {'form': form, 'password_form': password_form}
    return render(request, 'accounts/profile.html', context)
