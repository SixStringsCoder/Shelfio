from django.shortcuts import render, redirect
from .models import Collectible, Collection, Category, User
from .forms import CollectionModelForm, CollectibleModelForm, LinkModelForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


def category(request, username):
    """
    All of a user's Collections View

    """

    context = {'category': category}
    return render(request, 'collection/collections.html', context)


def collections(request, username):
    """
    All of a user's Collections View

    """

    collections = Collection.objects.filter(owner__username=username)
    context = {'category': category, 'collections': collections}
    return render(request, 'collection/collections.html', context)


@login_required  # Uses Django module to require login and disallow anonymous posting
def collection_form(request, username):
    """
    Collection form view

    """

    if request.method == "GET":
        form = CollectionModelForm()

    elif request.method == "POST":
        form = CollectionModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            collection = form.save(commit=False) # no blank or invalid data submissions
            # auto sets Collection "owner" to User account
            collection.owner = request.user

            # time stamp creation of collectible
            collection.created = timezone.now()
            # Add non-required additions to instance if needed
            collection.save()
            # Django Message module
            messages.add_message(request, messages.SUCCESS, f'The Collection {collection.name} has been added successfully.')
            return redirect(f'/collection/{collection.slug}/')


    context = {'form': form}
    return render(request, 'collection/collection_form.html', context)


def collection(request, username, collection_slug):
    """
    Collection Page Template View

    """

    collection = Collection.objects.get(slug=collection_slug)
    collectibles = collection.items.all()
    context = {'collection': collection, 'collectibles': collectibles}
    return render(request, 'collection/collection.html', context)


@login_required  # Uses Django module to require login and disallow anonymous posting
def collectible_form(request, username):
    """
    Collectible form View

    """

    if request.method == "GET":
        form = CollectibleModelForm()

    elif request.method == "POST":
        form = CollectibleModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            collectible = form.save(commit=False) # no blank or invalid data submissions
            # time stamp creation of collectible
            collectible.created = timezone.now()
            # Add non-required additions to instance if needed
            collectible.save()
            # Django Message module
            messages.add_message(request, messages.SUCCESS, f'{collectible.name} has been added successfully.')
            return redirect(f'collectible/{collectible.slug}/')
    # else:
    #     messages.add_message(request, messages.ERROR, f'{collectible.name} has been added successfully.')
    #     return redirect(f'/collections/{collectible.slug}/')

    context = {'form': form}
    return render(request, 'collection/collectible_form.html', context)


def collectible(request, username, collectible_slug):
    """
    A single collectible display view

    """

    collectible = Collectible.objects.get(slug=collectible_slug)
    context = {'collectible': collectible}
    return render(request, 'collection/collectible.html', context)


def collectible_edit(request, username, collectible_slug):
    """
    A single collectible edit view

    """
    collectible = Collectible.objects.get(slug=collectible_slug)  # Shows collectible details as editable fields

    form = CollectibleModelForm(instance=collectible, data=request.POST or None)
    if form.is_valid():
        collectible = form.save(commit=False)  # no blank or invalid data submissions
        # # time stamp creation of collectible
        # collectible.edited = timezone.now()
        # Add non-required additions to instance if needed
        collectible.save()
        # Django Message module
        messages.add_message(request, messages.SUCCESS, f'{collectible.name} has been edited successfully.')
        return redirect(f'collectible/{collectible.slug}/')

    context = {'form': form}
    return render(request, 'collection/collectible_edit.html', context)


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
