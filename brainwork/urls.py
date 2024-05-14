from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('posmove/',views.posmove,name='posmove'),
    path('play/',views.play,name='play')
]