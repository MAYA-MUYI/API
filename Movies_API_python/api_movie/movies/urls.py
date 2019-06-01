"""api_movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from movies import views

urlpatterns = [
    path('movies/', views.getMovies, name="home"),
    path('movies/<int:movie_id>', views.getMoviesDetail, name="detail"),
    path('movies/cinemas/<int:movie_base_id>', views.getCinemas, name="cinemas"),
    path('movies/cinemas/<int:movie_base_id>/<int:cinema_id>', views.getCinemasDetail, name="cinemas_detail"),
    path('movies/cinemas/<int:movie_base_id>/<int:cinema_id>/choose_seats', views.chooseSeat, name="choose"),
]
