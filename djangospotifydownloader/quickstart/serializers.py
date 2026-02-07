from django.contrib.auth.models import Group, User
from rest_framework import serializers

from djangospotifydownloader.quickstart.models import SpotifyLink

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpotifyLink
        fields = ["link"]
