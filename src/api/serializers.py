# Import the serializer method from the django_rest_framework
# Create a new Class regarding the API
# Import the models

from rest_framework import serializers
from .models import userinfo


class userinfo_serializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = '__all__'
