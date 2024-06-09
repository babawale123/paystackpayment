from rest_framework import serializers
from .models import StreamModel,WatchModel,ReviewModel

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewModel
        fields = "__all__"


class WatchSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    platform_name = serializers.ReadOnlyField(source='platform.name')
    class Meta:
        model = WatchModel
        fields = '__all__'

class StreamSerializer(serializers.ModelSerializer):
    watchlist = WatchSerializer(many=True, read_only=True)

    class Meta:
        model = StreamModel
        fields = '__all__'