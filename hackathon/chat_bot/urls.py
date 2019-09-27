from django.urls import path
from . import views
urlpatterns = [
    path('chat/',views.chat, name='chat'),
    path('room_chat/',views.room_chat, name='room_chat'),
]