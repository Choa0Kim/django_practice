from django.shortcuts import render
import random

# 파이썬(views.py)에서 데이터를 다 만들어서 html에 넘기는게 더 쉬움

def index(request):
    context = {
        'name': 'Jane',
        'login': True,
        'nums': [1, 2, 3, 4, 5, 6],
    }
    return render(request, 'articles/index.html', context)

#1. 값울 파이썬으로 만들어서 html에 넘겨줌 {{ key }}
#2. 필터 {{ | }} =>
#3. tag 


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,  #이름 달라도 됨.
    }
    return render(request, 'articles/dinner.html', context) # context를 렌더함수의 3번째 인자로 넣어줘야 함.


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


# 사용자 입력 데이터를 추출해서 응답 페이지에 보여주기
def catch(request):
    # 사용자 입력데이터는 대체 어디에 있을까? -> request 객체
    print(request.GET)  # <QueryDict: {'message': ['ssafy']}>
    print(request.GET.get('message'))  # ssafy
    message = request.GET.get('message')
    
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


def detail(request, num):  #urls.py 지정한 num과 같은 명으로 매개변수 지정해야 함.
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)