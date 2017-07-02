"""Shelfio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from accounts.api import UserViewSet
from collection.api import CollectionViewSet, CollectibleViewSet
from collection.views import home, base, contact, about, collections_public

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'collections', CollectionViewSet)
router.register(r'collectibles', CollectibleViewSet)


urlpatterns = [
    url(r'^base', base, name='base'),

    # The Admin
    url(r'^admin/', admin.site.urls),

    # Accounts
    url(r'accounts/', include('accounts.urls', namespace='accounts')),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', home, name='home'),
    url(r'^contact', contact, name='contact'),
    url(r'^about', about, name='about'),

    # public view (i.e. not logged-in) of Collections
    url(r'^public/(?P<status>[A-Z]+)/', collections_public, name='collections_public_gallery'),

    # Collection App User Specific
    url(r'^(?P<username>[a-z0-9_]+)/', include('collection.urls', namespace="collections")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Note below example is from Django 1.5
#     urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))
