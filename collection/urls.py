from django.conf.urls import url
from .views import (collection, collectible_form, collectible, collectible_edit,
                    collection_form, category, collections, collection_embed,)


urlpatterns = [
    # All of User's Collections View
    # TODO: Change Category to Gallery or Collections

    # url(r'collections/public', collections_public, name='collections_public_gallery'),  # public view
    url(r'collections/', collections, name='collections_gallery'),  # view


    # Collections Form, View, Embed View
    url(r'^collection/create/$', collection_form, name='collection_form'),   # form
    url(r'collection/(?P<collection_slug>[a-z0-9\-]+)/', collection, name='collection_detail'),  # view
    url(r'collection_embed/(?P<collection_slug>[a-z0-9\-]+)/', collection_embed, name='collection_embed'), # embed view - less styling


    # Collectible View, Form, and Edit
    url(r'^collectible/create/$', collectible_form, name='collectible_form'),  # form
    url(r'collectible/(?P<collectible_slug>[a-z0-9\-]+)/$', collectible, name='collectible_detail'),  # detail
    url(r'^collectible/edit/(?P<collectible_slug>[a-z0-9\-]+)/$', collectible_edit, name='collectible_edit'),  # edit
]
