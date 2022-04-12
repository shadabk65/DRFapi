from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from DRFapp.models import WatchList, StreamPlatform, Review
from DRFapp.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
# from rest_framework import mixins
from rest_framework import generics



class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
    	pk = self.kwargs['pk']
    	return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer





# class ReviewDetail( mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


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





#function based view

# @api_view(['GET', 'POST'])
# def movie_list(request):

# 	if request.method == 'GET':
# 		movies = MovieList.objects.all()
# 		serializer = MovieSerializer(movies, many=True)
# 		return Response(serializer.data)

# 	if request.method == 'POST':
# 		serializer = MovieSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		else:
# 			return Response(serializer.errors)



# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

# 	if request.method == 'GET':

# 		try:
# 			Singlemovie = MovieList.objects.get(pk=pk)
		
# 		except MovieList.DoesNotExist:
# 			return Response({ "error": "movie not found" }, status=status.HTTP_404_NOT_FOUND)
		
		
# 		serializer = MovieSerializer(Singlemovie)
# 		return Response(serializer.data)

# 	if request.method == 'PUT':
# 	    	Singlemovie = MovieList.objects.get(pk=pk)
# 	    	serializer = MovieSerializer(Singlemovie, data= request.data)
# 	    	if serializer.is_valid():
# 	    		serializer.save()
# 	    		return Response(serializer.data)
# 	    	else:
# 	    		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	if request.method == 'DELETE' :
# 		Singlemovie = MovieList.objects.get(pk=pk)
# 		Singlemovie.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)