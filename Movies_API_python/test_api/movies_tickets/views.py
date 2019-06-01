#coding=utf8
import random
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response

from movies_tickets.models import MovieBase, MovieDetail, Cinemas
from movies_tickets.serializers import MovieBaseSerializer, MovieDetailSerializer, CinameSerializer


star = [8.8, 9.0, 9.1, 9.3]
step = [3, 4, 5]

class MovieBaseAPI(APIView):
    """
    电影清单API
    """
    serializer_class = MovieBaseSerializer

    def get(self, request):
        """
        获取电影信息
        """
        result = []
        movies = MovieBase.objects.all()

        for movie in movies:
            result.append({
                'movie_base_id': movie.id,
                'movie_name': movie.movie_name,
                'time': movie.time,
                "star": random.choice(star),
                'vision': movie.vision,
                'ellipsis': movie.ellipsis,
                "type": MovieDetail.objects.get(id=movie.id).type,
                "pic": "image/" + movie.movie_name + '_pic.jpg',
                "ellipsis_length": len(movie.ellipsis)
            })
        return Response(result)


class MovieDetailAPI(APIView):
    """
    电影列表API
    """
    serializer_class = MovieDetailSerializer

    def get(self, request, movie_id):
        """
        获取电影列表
        """
        result = []
        _movie = MovieBase.objects.get(id=movie_id)
        movies = MovieDetail.objects.filter(movie_name=_movie.movie_name)
        for movie in movies:
            result.append({
                'movie_detail_id': movie.id,
                'movie_base_id': _movie.id,
                'movie_name': movie.movie_name,
                'time': movie.time,
                "star": random.choice(star),
                "type": movie.type,
                'vision': movie.vision,
                'ellipsis': movie.ellipsis,
                "ellipsis_length": len(movie.ellipsis),
                "duration": movie.duration,
                'introduction': movie.introduction,
                'timg': 'image/' + movie.movie_name + '_timg.jpg',
                'pic': 'image/' + movie.movie_name + '_pic.jpg',
                'stills1': 'image/' + movie.movie_name + '_stills1.jpg',
                'stills2': 'image/' + movie.movie_name + '_stills2.jpg',
                'stills3': 'image/' + movie.movie_name + '_stills3.jpg',
                'stills4': 'image/' + movie.movie_name + '_stills4.jpg',
            })

        return Response(result)


class CinemasApi(APIView):

    def get(self, request, movie_base_id):
        """
        获取电影院信息
        """
        result = []
        movie = MovieBase.objects.get(id=movie_base_id)
        cinemas = Cinemas.objects.all()
        for cinema in cinemas:
            result.append({
                "cinema_id": cinema.id,
                "cinema_name": cinema.cinema_name,
                "movie_base_id": movie.id,
                "movie_name": movie.movie_name,
                "city": cinema.city,
                "address": cinema.address,
                "price": cinema.price,
                "distance": 13.77 + (cinema.id - 1) * random.choice(step)
            })
        return Response(result)




class CinemaDetailAPI(APIView):

    serializer_class = CinameSerializer

    def get(self, request, movie_id, ciname_id):
        """
        获取城市行政区列表
        """
        result = []
        _movie = MovieBase.objects.get(id=movie_id)
        movie = MovieDetail.objects.get(movie_name=_movie.movie_name)
        cinema = Cinemas.objects.get(id=ciname_id)
        result.append({
            "movie_base_id": movie_id,
            "movie_name": movie.movie_name,
            "vision": movie.vision,
            "cinema_id": ciname_id,
            "cinema_name": cinema.cinema_name,
            "time": movie.time[-5:],
            "price": cinema.price,
            "duration": movie.duration
        })

        return Response(result)

#
# class CinemaListAPI(APIView):
#     """
#     影院列表API
#     """
#     serializer_class = CinemaListSerializer
#
#     def get(self, request):
#         """
#         获取影院列表
#         """
#         serializer = self.serializer_class(data=request.query_params)
#         serializer.is_valid(raise_exception=True)
#         city_id = serializer.validated_data.get('city_id')
#         dic = {
#             'meituan_district_id': serializer.validated_data.get('meituan_district_id'),
#             'meituan_movie_id': serializer.validated_data.get('meituan_movie_id'),
#             'nuomi_district_id': serializer.validated_data.get('nuomi_district_id'),
#             'nuomi_movie_id': serializer.validated_data.get('nuomi_movie_id'),
#             'taobao_district_id': serializer.validated_data.get('taobao_district_id'),
#             'taobao_movie_id': serializer.validated_data.get('taobao_movie_id'),
#         }
#
#         try:
#             cinema_list = CinemaList(city_id, **dic)
#         except ObjectDoesNotExist:
#             return DoesNotExistResponse()
#         except:
#             return UnKnownResponse()
#
#         task_result = cinema_list.get_cinema_list()
#         return Response(task_result)
#
#
# class PriceListAPI(APIView):
#     """
#     价格列表API
#     """
#     serializer_class = PriceListSerializer
#
#     def get(self, request):
#         """
#         获取价格列表
#         """
#         serializer = self.serializer_class(data=request.query_params)
#         serializer.is_valid(raise_exception=True)
#         city_id = serializer.validated_data.get('city_id')
#         dic = {
#             'meituan_movie_id': serializer.validated_data.get('meituan_movie_id'),
#             'meituan_cinema_id': serializer.validated_data.get('meituan_cinema_id'),
#             'nuomi_movie_id': serializer.validated_data.get('nuomi_movie_id'),
#             'nuomi_cinema_id': serializer.validated_data.get('nuomi_cinema_id'),
#             'taobao_movie_id': serializer.validated_data.get('taobao_movie_id'),
#             'taobao_cinema_id': serializer.validated_data.get('taobao_cinema_id'),
#         }
#         try:
#             price_list = PriceList(city_id, **dic)
#         except ObjectDoesNotExist:
#             return DoesNotExistResponse()
#         except:
#             return UnKnownResponse()
#         task_result = price_list.get_price_list()
#         return Response(task_result)
