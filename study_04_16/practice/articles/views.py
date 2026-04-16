from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import ArticleForm
from .models import Article

# 디버깅 시험
# 코드주고 버그/에러 고치는 문제. 

# 무조건 웹의로 리턴해주는 값이 있어야 함.
def index(request):
    print("index로 들어옴") #print로 함수 잘 찍히는지 확인

    # TODO: 게시글 전체 목록을 전달 & 출력
    # order_by('-created_at') =>내림차순
    articles = Article.objects.all().order_by('-created_at')

    filter_type = request.GET.get("filter", "all")
    if filter_type == 'public':
        articles = articles.filter(is_public=True)

    context = {
        "articles": articles,
        "filter_type": filter_type
    }
    return render(request, "articles/index.html", context)
    # return render(request, "index.html") 
    # =>한 단게(articles) 더 들어가서 작성한 이유 => 다른 앱에 같은 index.html이 있을 경우 구분하기 위해
    # (구분이 안되면 settings.py에서 먼저 적힌 앱을 기준으로 불러옴)

# 1. GET 요청 - 생성 페이지를 출력
# 2. POST 요청 - DB에 저장
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # TODO: DB 저장
        form = ArticleForm(request.POST)

        #유효성 검사하고 저장
        if form.is_valid():
            form.save()
            # 게시글 목록으로 이동
            return redirect("articles:index")
            # return render(request, "articles/index.html") => 정상적인 페이지 이동이 아님.
            # redirect: post->get
    else:
        # TODO: 생성 페이지 출력
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, "articles/create.html", context)
    

def detail(request, pk):
    # article = Article.objects.get(pk=pk) => 없는 pk를 조회하면 오류남
    article = get_object_or_404(Article, pk=pk)

    article.view_count += 1 #db에 반영 필요
    article.save(update_fields=["view_count"]) #어떤 데이터가 변화하는지 같이 넣어줌

    
    context = {
        'article': article,
    }

    return render(request, "articles/detail.html", context)
# 삭제는 보통 delete http method를 form 태그로 구현 ㅌ
# - delete 대신 post로 한다.
@require_http_methods(['POST'])
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("articles:index")

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        
   
        form = ArticleForm(request.POST, instance=article) #instance=>데이터를 어떤걸 기준으로 폼을 채울 것인지 설정

        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.id)
    else:

        form = ArticleForm(instance=article)
            

     # 내어쓰기?한 이유 시험  => 유효성 검증 때문에?
    context = {
        'form': form,
        'article': article,
    }

    return render(request, "artcles/update.html", context)


# 5.1 페이지 종류
# - - base.html 
# - 게시글 목록 페이지
# - 게시글 상세 페이지
# - 생성 페이지
# - 수정 페이지