from rest_framework import serializers
from DRFapp.models import WatchList, StreamPlatform


# model serializer


class WatchListSerializer(serializers.ModelSerializer):

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

