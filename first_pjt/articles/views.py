from django.shortcuts import render
from django.http import JsonResponse


# def index():
#     pass 

# url에서 호출하는 함수의 첫 번째 파라미터는 항상 request
# request: 사용자의 요청 정보가 모두 들어있음.

# def index(request):
#     return render(request, 'articles/index.html')

def index(request):
    print("index 함수")
    return JsonResponse({"응답": "articles 의 index 함수"})


# GET '/articles/'  => 서버주소/aricles/로  get 요청을 보냈다
#-GET -조회
#-POST - 생성
#-UPDATE - 수정
#-DELETE - 삭제