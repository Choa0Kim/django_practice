from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializer import ArticleSerializer

# Create your views here.
# 모든 DRF의 뷰함수는 반드시 api_view 데코레이터가 필수
@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        #1.1 전체 게시글 조회(DB)
        articles = Article.objects.all()
        # 그런데 articles는 쿼리셋 형식이여서 다른 서비스들은 이 타입을 사용할 수 없음
        # 이때, 직렬화를 진행해서 유연한 데이터 형식으로 변환
        #1.2 직렬화 
        # 원물 데이터가 단일 데이터가 아닌 형식이면 many옵션을 True로 변경
        serializer = ArticleSerializer(articles, many=True)
        # 1.3. 직렬화된 데이터 덩어리에서 게시글 데이터만 추출해서 응답
        return Response(serializer.data)
    # 2. 데이터 생성 관련 처리
    elif request.method == 'POST':
        # 2.1사용자가 보낸 데이터를 직렬화
        # 과거에는 request.POST에서 추출했지만, DRF에서는 request.data를 사용
        serializer = ArticleSerializer(data=request.data)
        #2.2 유효성 검사
        if serializer.is_valid():
            #2.3 저장
            serializer.save()
            # 2.4 저장 후 201 상태 코드로 응답
            return Response(serializer.data, status.HTTP_201_CREATED)
        # 2.5 유효성 검사 실패했다면 400 상태 코드로 응답
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
        
            



@api_view(['GET'])
def article_detail(request, article_id):
    if request.method == 'GET':
        # 1.1 단일 게시글 조회
        article = Article.objects.get(pk=article_id)
        # 2.1 직렬화
        serializer = ArticleSerializer(article)
        # 3.1 직렬화된 데이터에서만 필요한 데이터만 추출하여 응답
        return Response(serializer.data)
    elif request.method == 'DELETE':
        pass:
        elif
    return Response(serializer.data, status.)
    
