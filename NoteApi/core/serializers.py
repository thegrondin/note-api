from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from NoteApi.core.models import User, Note


class NoteSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["date_created", "title"]


class UserSerializer(serializers.HyperlinkedModelSerializer):

    notes = NoteSummarySerializer(many=True)

    class Meta:
        model = User
        fields = ["email", "firstname", "lastname"]


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ["user", "date_created", "title", "content"]