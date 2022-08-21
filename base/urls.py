from django.urls import path
from . import views as base_views

urlpatterns = [
    path('login/', base_views.login_page, name="login"),
    path('logout/', base_views.logout_user, name="logout"),
    path('register/', base_views.register_page, name="register"),
    path('', base_views.home_view, name="home-view"),
    path('room/<str:pk>/', base_views.room_view, name="room-view"),
    path('create-room', base_views.create_room, name="create-room"),
    path('update-room/<str:pk>/', base_views.update_room, name="update-room"),
    path('delete-room/<str:pk>/', base_views.delete_room, name="delete-room"),
    path('delete-message/<str:pk>/', base_views.delete_message, name="delete-message"),

]
