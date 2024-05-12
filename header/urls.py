from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('posmove/',views.posmove),
    path('play/',views.play)
]