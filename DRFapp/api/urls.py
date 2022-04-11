from django.urls import path, include
# from DRFapp.api.views import movie_list, movie_details
from DRFapp.api.views import WatchListAv, WatchDetailAv, StreamPlatformaList, StreamPlatformDetailAv

urlpatterns = [
    path('list/', WatchListAv.as_view() , name= 'movie-list'),
    path('list/<int:pk>', WatchDetailAv.as_view() , name= 'movie-details'),

    path('stream/', StreamPlatformaList.as_view() , name= 'stream'),
    path('stream/<int:pk>', StreamPlatformDetailAv.as_view() , name= 'stream-detail'),


]