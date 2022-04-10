from rest_framework import serializers
from DRFapp.models import Movie as MovieList


# model serializer


class MovieSerializer(serializers.ModelSerializer):

	len_name = serializers.SerializerMethodField()


	class Meta:
		model = MovieList
		fields = "__all__"

	def get_len_name(self, object):
  	 length = len(object.name) 
  	 return length

	def validate_name(self, value):
		if len(value) < 2 :
			raise serializers.ValidationError("name is to short")
		else:
			return value

#object level validation

	def validate(self, data):
		if data ['name'] == data ['description']:
			raise serializers.ValidationError("Title and description should be different")
		else:
			return data


# def name_length(value):
# 	if len(value) < 2:
# 		raise serializers.ValidationError("name is too short!")

# class MovieSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(validators= [name_length])
# 	description = serializers.CharField()
# 	active = serializers.BooleanField()


# 	def create(self, validated_data):
# 		return MovieList.objects.create(**validated_data)


# 	def update(self, instance, validated_data):
# 		instance.name = validated_data.get('name', instance.name)
# 		instance.description = validated_data.get('description', instance.description)
# 		instance.active = validated_data.get('active', instance.active)
# 		instance.save()
# 		return instance

# field level validation

	# def validate_name(self, value):
	# 	if len(value) < 2 :
	# 		raise serializers.ValidationError("name is to short")
	# 	else:
	# 		return value

# object level validation

	# def validate(self, data):
	# 	if data ['name'] == data ['description']:
	# 		raise serializers.ValidationError("Title and description should be different")
	# 	else:
	# 		return data
