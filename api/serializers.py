from rest_framework import serializers
from .models import StreamModel,WatchModel,ReviewModel

class ReviewSerializer(serializers.ModelSerializer):
    movie_name = serializers.ReadOnlyField(source="watchlist.title")
    user = serializers.StringRelatedField()

    class Meta:
        model = ReviewModel
        exclude = ('watchlist',)


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