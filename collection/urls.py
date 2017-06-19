from django.conf.urls import url
from .views import collection, collectible_form


urlpatterns = [

    # Categories
    url(r'categories/', collection, name='categories'),             # All, List cats

    url(r'$', collection, name='category'),  # detail / list


    # Collections
    # url(r'shelf/(?P<slug>\w+)/', collection, name='category'),     # detail / list

    # Collectible
    url(r'shelf/(?P<collection_slug>\w+)/', collection, name='collection'),   # detail
    url(r'^shelf/create', collectible_form, name='collectible'),

]


