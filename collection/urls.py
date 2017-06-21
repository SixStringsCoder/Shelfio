from django.conf.urls import url
from .views import collection, collectible_form, collectible


urlpatterns = [

    # Categories
    # url(r'categories/', collection, name='categories'),             # All, List cats
    #
    # url(r'$', collection, name='category'),  # detail / list


    # Collections
    # url(r'shelf/(?P<slug>\w+)/', collection, name='category'),     # detail / list

    # Collectible View, Form, and Edit
    url(r'^collectible/create', collectible_form, name='collectible_form'),  # form
    url(r'(?P<collectible_slug>[a-z0-9\-]+)/$', collectible, name='collectible_detail'), # detail
]
