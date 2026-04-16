from django.urls import path
from . import views #현재 폴더에 있는 views.py를 확인?

urlpatterns = [
    path('', views.index),

 
]