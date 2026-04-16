from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form, 
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save() # 저장이 완료된 데이터의 인스턴스를 반환
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm() # post가 아닌 경우

    context = {
            'form': form,
        }
    return render(request, 'articles/create.html', context)
    

    # form = ArticleForm(request.POST)  #사용자의 입력이 채워진 FORM  생성
    # if form.is_valid(): # T/F
    #     # 유효성 검사를 통과 한다면?
    #     # DB 저장
    #     article = form.save() # 저장이 완료된 데이터의 인스턴스를 반환
    #     return redirect('articles:detail', article.pk)
    # # 유효성 검사를 통과하지 못한 경우 (+ 에러 메세지)
    # context = {
    #     'form': form,
    # }
    # return render(request, 'articles/new.html', context)

    # title = request.GET.get('title') 
    # content = request.GET.get('content')
    # title = request.POST.get('title')       # GET에서 POST로 요청 변경
    # content = request.POST.get('content')   # GET에서 POST로 요청 변경
    # # 1. 인스턴스 생성 후 속성 할당 및 저장
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 2. 인스턴스 생성 시 속성 할당 후 저장
    # article = Article(title=title, content=content)
    # article.save()

    # # 3. create() 메서드를 통한 인스턴스 생성 및 즉시 저장
    # # Article.objects.create(title=title, content=content)
    
    # # return render(request, 'articles/create.html')

    # return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     form = article = Article(request.POST, isinstance=article)

#     if form.is_vaild():
#         form.save()
#         return redirect('articles:detail', article.pk)
    
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

    # article = Article.objects.get(pk=pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()

def update(request, pk):
    # DB에 수정하고 싶은 글을 하나 가져옴(수정 대상)
    article = Article.objects.get(pk=pk)
    # 만약 사용자가 수정완료 버튼늘 눌러서 데이터를 보낸다면(post 방식)
    if request.method == 'POST':
        # 
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles"detail', article.pk)
    else:
        form =ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form, 
    }
    return render(request, 'articles/update.html', context)   