from django.urls import path
from . import views as base_views

urlpatterns = [
    path('', base_views.home_view, name="home-view"),
    path('room/<str:pk>', base_views.room_view, name="room-view")
]
