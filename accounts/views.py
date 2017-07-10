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
        form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            # Add non-required additions to instance if needed
            user.save()

            send_mail(
                subject='You have a Shelfio account!',
                message=f'Sign in {request.user} and get organized!  Share your Collections with friends!',
                from_email='rshanlon3@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)

            return redirect('/')  # TODO: success redirect to some web page

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required()
def profile(request):
    """
    Update User Info Form

    """
    password_form = PasswordChangeForm(user=request.user)
    if request.method == 'GET':
        form = CustomUserUpdateForm(instance=request.user)

    elif request.method == 'POST':
        form = CustomUserUpdateForm(instance=request.user, data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Add non-required additions to instance if needed
            user.save()

            messages.add_message(request, messages.ERROR, f'Your user profile is updated!')
            return redirect(f'/accounts/profile/')

    context = {'form': form, 'password_form': password_form}
    return render(request, 'accounts/profile.html', context)


@login_required()
def reset_pw(request):
    """
    Update User Password Form

    """

    if request.method == 'POST':
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if password_form.is_valid():
            user = password_form.save(commit=False)
            # Add non-required additions to instance if needed
            user.save()

            send_mail(
                subject='Your Shelfio Password!',
                message=f'{request.user}, your Shelfio password just changed! '
                        f'Now, log in and get organized, yo!',
                from_email='rshanlon3@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            username = password_form.cleaned_data.get('username')
            raw_password = password_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)

            messages.add_message(request, messages.INFO, f'Your password is updated!')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, f'{password_form.errors}')
            return redirect('profile')
