from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


# REST ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer