from django.shortcuts import render


def home(request):
    """
    Landing page Template View

    """

    return render(request, 'home.html')


