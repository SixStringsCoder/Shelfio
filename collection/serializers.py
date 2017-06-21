from rest_framework import serializers
from .models import Collection, Collectible


class CollectibleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collectible
        depth = 1
        fields = ('collection', 'name', 'creator', 'created',)

# REST ViewSets define the view behavior.
class CollectionModelSerializer(serializers.ModelSerializer):
    collectibles = CollectibleModelSerializer(many=True)

    class Meta:
        model = Collection
        depth = 1
        fields = ('name', 'slug', 'type', 'categories', 'created', 'modified', 'collectibles', )

       # TODO
    # def get_collection(self, obj):




