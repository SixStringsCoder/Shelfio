from rest_framework import viewsets
from .models import Collection, Collectible
from .serializers import CollectionModelSerializer, CollectibleModelSerializer


# REST ViewSets define the view behavior.
class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    model = Collection
    queryset = Collection.objects.all()
    serializer_class = CollectionModelSerializer


class CollectibleViewSet(viewsets.ReadOnlyModelViewSet):
    model = Collectible
    queryset = Collectible.objects.all()
    serializer_class = CollectibleModelSerializer


