from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article

def index(request):
    # 모든 게시글 정보를 가져옴    
    articles = get_list_or_404(Article)
    context = {
        'articles': articles,

    }
    return render(request, 'articles/index.html', context)

def detail(request, article_id):
    articles =  Article.objects.get(pk=article_id)  #api 요청 쿼리?
    context = {
        'articles': articles,

    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 사용자의 입력 정보를 받아서 DB에 저장

    # 첫번째 방식
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.content = content
    article.title= title
    article.save()

    # 두번째 방식
    # article = Article(title=title, content=content)
    # article.save()

    # #세번째 방식
    # article = Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')





