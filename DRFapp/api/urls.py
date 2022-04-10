from django.urls import path, include
# from DRFapp.api.views import movie_list, movie_details
from DRFapp.api.views import MovieListAv, MovieDetailAv

urlpatterns = [
    path('list/', MovieListAv.as_view() , name= 'movie-list'),
    path('<int:pk>', MovieDetailAv.as_view() , name= 'movie-details'),

]