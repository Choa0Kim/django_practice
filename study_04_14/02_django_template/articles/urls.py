from django.urls import path
from articles import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name = "index"),
    path('dinner/', views.dinner, name = "dinner"),
    path('search/', views.search, name = "search"),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('articles/<int:num>/', views.detail),  #views.py 에도 num (같은 명)으로 매개 변수 선언해야 함.
    path('hello/<str:name>/', views.greeting, name='greeting'),
   
]
