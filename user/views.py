from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from django.http.response import Http404

from .models import User
from .serizlizers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, **kwargs)
