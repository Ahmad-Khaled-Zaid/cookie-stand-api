from rest_framework import serializers
from .models import Marshmello


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marshmello
        fields = "__all__"
