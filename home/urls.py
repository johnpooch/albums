from django.urls import path
from home.views import get_index, add_music

urlpatterns = [
    path('', get_index),
    path('add_music/', add_music, name='new_post'),
    ]