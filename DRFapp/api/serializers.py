from rest_framework import serializers
from DRFapp.models import WatchList, StreamPlatform, Review


# model serializer

class ReviewSerializer(serializers.ModelSerializer):

	class Meta:
		model = Review
		fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):

	reviews = ReviewSerializer(many=True, read_only=True)


	class Meta:
		model = WatchList
		fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

 # watchlist= serializers.HyperlinkedRelatedField(
 #        many=True,
 #        read_only=True,
 #        view_name='movie-details'
 #    )

	watchlist = WatchListSerializer(many=True, read_only=True)

	class Meta:
		model = StreamPlatform
		fields = "__all__"
