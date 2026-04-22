from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST

from django.contrib import messages #세션레벨에서 메세지를 담아놓고 사용
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def index(request):
    return render(request, "accounts/index.html")


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        #Log 레벨
        # - DEBUG / INFO / SUCCESS / WARING /ERROR
        messages.warning(request, "이미 로그인된 사용자입니다!")
        return redirect("accounts:index")
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect("accounts:index")
    # POST: 실제 로그인
    # - 유효성 검증
    # - DB에 있는 유저를 검색 -> 패스워드 검증
    # - 세션 데이터 생성 + 쿠키에 저장 -> 해당 쿠키와 함께 응답
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # 로그인
            # 만약 url에 next가 있다면, 해당 위피치로 이동
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)


            # 없다면 메인페이지로 이동
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, "accounts/login.html", context)


# 로그아웃
# - DB에 세션 데이터 삭제
# - 쿠키에서 세션 데이터 삭제
@require_POST  
# @login_required  #안쪽에 있는 데코레이션이 먼저 처리됨. 순서중요. 근데 보통 로그아웃에는 달지 않음. 405에러 발생
def logout(request):
    auth_logout(request)
    return redirect("accounts:index")

# 기본 로그인 페이지(accounts/login/)로 이동
#로그인된 사용자만 들어와라
@login_required(login_url="accounts:login")
def profile(request):
    #유저 정보 조회
    # profile.html 로 전달
    return render(request, "accounts/profile.html")