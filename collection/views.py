from django.shortcuts import render, redirect
from .models import Collectible, Collection, Category
from .forms import CollectibleModelForm, LinkModelForm
from django.utils import timezone
from django.contrib import messages



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
    context = {'collection': collection}
    return render(request, 'collection.html', context)


def collectible_form(request):
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
            messages.add_message(request, messages.SUCCESS, f'{collectible.name} has been added successfully to {collection.name}.')
            return redirect(f'/collections/{collectible.slug}/')
    # else:
    #     messages.add_message(request, messages.ERROR, f'{collectible.name} has been added successfully.')
    #     return redirect(f'/collections/{collectible.slug}/')

    context = {'form': form}
    return render(request, 'collectible_form.html', context)


def collectible(request, collectible_slug):
    """
    A single collectible display view

    """

    collectible = Collectible.objects.get(slug=collectible_slug)
    context = {'collectible': collectible}
    return render(request, 'collectible.html', context)


def collectible_edit(request, pk):
    """
    A single collectible edit view

    """

    collectible = Collectible.objects.get(id=pk)
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
