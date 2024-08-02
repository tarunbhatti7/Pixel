from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
    path('chat/lobby/', views.LobbyView.as_view(), name='lobby'),
    path('chat/room/<slug:room_slug>', views.RoomView.as_view(), name='room'),
    path('chat/create/', views.create_room_view, name='create-room'),
    path('chat/join-room/', views.join_room, name='join-room'),
    path('chat/remove-room/', views.remove_room, name='remove-room'),
]
