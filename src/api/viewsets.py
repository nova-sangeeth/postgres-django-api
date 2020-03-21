from rest_framework import viewsets
from . import models
from . import serializers


class userinfo_viewset(viewsets.ModelViewSet):
    queryset = models.userinfo.objects.all()
    serializer_class = serializers.userinfo_serializer
