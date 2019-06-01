from django.shortcuts import  get_object_or_404, render
import requests
import json

def getMovies(request):
    url = "http://127.0.0.1:8000/movies"
    data = json.loads(requests.get(url).text, encoding='utf-8')

    context = {
        "datas": data
    }
    return render(request, 'movie/index.html', context)


def getMoviesDetail(request, movie_id):
    url = "http://127.0.0.1:8000/movies/" + str(movie_id)
    data = json.loads(requests.get(url).text, encoding='utf-8')

    context = {
        "datas": data
    }
    return render(request, 'movie/details.html', context)


def getCinemas(request, movie_base_id):
    url = "http://127.0.0.1:8000/cinemas/" + str(movie_base_id)
    data = json.loads(requests.get(url).text, encoding='utf-8')
    context = {
        "datas": data
    }
    return render(request, 'movie/film_cinema.html', context)


def getCinemasDetail(request, movie_base_id, cinema_id):
    url = "http://127.0.0.1:8000/cinemas/" + "movie_base_id=" + str(movie_base_id) + "/" + "cinema_id=" + str(cinema_id)
    data = json.loads(requests.get(url).text, encoding='utf-8')
    context = {
        "datas": data
    }
    return render(request, 'movie/tickets.html', context)


def chooseSeat(request, movie_base_id, cinema_id):
    url = "http://127.0.0.1:8000/cinemas/" + "movie_base_id=" + str(movie_base_id) + "/" + "cinema_id=" + str(cinema_id)
    data = json.loads(requests.get(url).text, encoding='utf-8')
    context = {
        "datas": data
    }
    return render(request, 'movie/choose_seat.html', context)