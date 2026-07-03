from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = routers.DefaultRouter()

router.register(r"movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>", ActorDetail.as_view(), name="actor_detail"),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>", GenreDetail.as_view(), name="genre_detail")
]

app_name = "cinema"
