from django.shortcuts import render
from .models import Collectible, Collection, Category


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


def category(request, slug):
    """
    All of a user's Collections View

    """

    category = Category.objects.get(slug=slug)
    context = {'category': category}
    return render(request, 'collections.html', context)


def collection(request, slug):
    """
    Collection Page Template View

    """

    collection = Collection.objects.get(slug=slug)
    context = { 'collection': collection}
    return render(request, 'collection.html', context)


def collectible_form(request):
    """
    Collectible form-field to enter details

    """

    return render(request, 'collectible_form.html')


def collectible_view(request, pk):
    """
    A single collectible display view

    """
    collectible =  Collectible.objects.get(id=pk)
    context = {'collectible': collectible}
    return render(request, 'collectible_view.html', context)


def collectible_edit(request, pk):
    """
    A single collectible edit view

    """
    collectible =  Collectible.objects.get(id=pk)
    context = {'collectible': collectible}
    return render(request, 'collectible_edit.html', context)


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
