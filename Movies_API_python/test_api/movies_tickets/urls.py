#coding=utf8

from django.conf.urls import url
from movies_tickets.views import MovieBaseAPI, MovieDetailAPI, CinemasApi, CinemaDetailAPI

urlpatterns = [
    url(r'^movies/$', MovieBaseAPI.as_view()),
    url(r'^movies/(\d+)/$', MovieDetailAPI.as_view()),
    url(r'^cinemas/(\d+)$', CinemasApi.as_view()),
    url(r'^cinemas/movie_base_id=(\d+)/cinema_id=(\d+)$', CinemaDetailAPI.as_view()),
    # url(r'^ticket/$', PriceListAPI.as_view()),
]