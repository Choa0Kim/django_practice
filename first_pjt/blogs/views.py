from django.shortcuts import render

# 게시글 정보를 변수에 저장
# - 서버가 켜질 때 자동으로 실행
posts = [
    {
        "post_id":1,
        "title": "블로그 동아리에 대해서",
        "content": "나의 깊은 내면과 마주하는 공간"

    },

    {
        "post_id":2,
        "title": "김지운은 누구?",
        "content": "가짜 뉴스 전문가"
    },
]
post_id = 3

# print("안녕요")
# 게시글 전체를 확인할 수 있는 페이지를 렌더링
# # render html을 그대로 브라우저에 그려줌?
# django templates language
def index(request):
    #django가 기본적으로 html 파일들을 "templates" 폴더에서 검색한다.
    
    greeting = "안녕하세요 그냥 블로그입니다."
    view_count = 5

    context = {
        'greeting':greeting,
        'view_count': view_count,
        'posts': posts,

    }

  
    return render(request, "blogs/index.html", context) 
