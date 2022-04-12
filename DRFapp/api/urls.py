from django.urls import path, include
# from DRFapp.api.views import movie_list, movie_details
from DRFapp.api.views import WatchListAv, WatchDetailAv, StreamPlatformaList, StreamPlatformDetailAv, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAv.as_view() , name= 'movie-list'),
    path('list/<int:pk>', WatchDetailAv.as_view() , name= 'movie-details'),

    path('stream/', StreamPlatformaList.as_view() , name= 'stream'),
    path('stream/<int:pk>', StreamPlatformDetailAv.as_view() , name= 'stream-detail'),

    path('stream/<int:pk>/review/', ReviewList.as_view() ),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name= 'review-detail' ),

]