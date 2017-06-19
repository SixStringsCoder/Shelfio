from django.shortcuts import render


def home(request):
    """
    Landing page Template View

    """

    return render(request, 'home.html')


def base(request):
    """
    Base Page Template View

    """

    return render(request, 'base.html')


def collection(request):
    """
    Collection Page Template View

    """

    return render(request, 'collection.html')



def collectible_form(request):
    """
    collectible/item form  View

    """

    return render(request, 'collectible_form.html')


def contact(request):
    """
    Contact Page View

    """

    return render(request, 'contact.html')


def about(request):
    """
    About Page View

    """

    return render(request, 'about.html')
