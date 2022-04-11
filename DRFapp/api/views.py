from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from DRFapp.models import WatchList, StreamPlatform
from DRFapp.api.serializers import WatchListSerializer, StreamPlatformSerializer


class StreamPlatformaList(APIView):

	def get(self, request):
		platform = StreamPlatform.objects.all()
		serializer = StreamPlatformSerializer(platform, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = StreamPlatformSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class StreamPlatformDetailAv(APIView):

	def get(self, request, pk):
		try:
			Singlemovie = StreamPlatform.objects.get(pk=pk)

		except StreamPlatform.DoesNotExist:
			return Response({ "error": "movie not found" }, status=status.HTTP_404_NOT_FOUND)
		
		
		serializer = StreamPlatformSerializer(Singlemovie)
		return Response(serializer.data)

	def put(self, request, pk):
		Singlemovie = StreamPlatform.objects.get(pk=pk)
		serializer = StreamPlatformSerializer(Singlemovie, data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk):
		Singlemovie = StreamPlatform.objects.get(pk=pk)
		Singlemovie.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)






class WatchListAv(APIView):

	def get(self, request):
		movies = WatchList.objects.all()
		serializer = WatchListSerializer(movies, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = WatchListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class WatchDetailAv(APIView):

	def get(self, request, pk):
		try:
			Singlemovie = WatchList.objects.get(pk=pk)

		except WatchList.DoesNotExist:
			return Response({ "error": "movie not found" }, status=status.HTTP_404_NOT_FOUND)
		
		
		serializer = WatchListSerializer(Singlemovie)
		return Response(serializer.data)

	def put(self, request, pk):
		Singlemovie = WatchList.objects.get(pk=pk)
		serializer = WatchListSerializer(Singlemovie, data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk):
		Singlemovie = WatchList.objects.get(pk=pk)
		Singlemovie.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

