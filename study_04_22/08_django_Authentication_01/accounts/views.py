from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    # 로그인한 사용자는 로그인할 필요가 없음
    if request.user.is_authenticated:
        return redirect('articels:index')
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    # return redirect('articels:index')
    return redirect('articles:index')


def signup(request):
    # 로그인한 사용지는 회원가입 필요 없음
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) #회원가입 후 로그인
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    
@login_required
def delete(request):
    # print(request.user.usename, 999999999999999999999999999999999)
    request.user.delete()
    auth_login(request) # 순서가 바뀌면 안됨
    return redirect('articles:index')