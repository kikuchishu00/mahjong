from .models import Stats
from rest_framework import serializers

class StatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stats
        fields = (
            'date',
            'points',
        )