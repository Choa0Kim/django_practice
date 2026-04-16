
from django.urls import path
from . import views   #현재 경로에 있는 views를 확인해라

# include=> 한 번 더 들어가서 확인해라
app_name ="articles"
urlpatterns = [

    path("", views.index, name="index"),
    
    # TODO - 게시글 상세 페이지 
    #  <>=> 변수
    path("<int:pk>/", views.detail, name="detail"),
    # TODO - 생성 페이지
    path("create/", views.create, name="create"),
    # TODO - 수정 페이지
    path("<int:pk>/update/", views.update, name="update"),
    # 삭제 페이지
    path("<int:pk>/delete/", views.delete, name="delete"),

]




# 1. 사용자가 접속 시 생성 페이지 출력
# 2. DB에 저장

