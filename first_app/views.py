import random # 파이썬이 기본으로 가지고있는 라이브러리(설치할 필요X)를 위에 씀
from faker import Faker
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html') # html을 랜더링(어떤 물건의 형태를 디지털화 시키는 것)하는 역할

def hello(request):
    my_name = 'dahee' # 변하는 데이터

    context = {
        'my_name': my_name,
    }

    return render(request, 'hello.html', context)
    # return render(request, 'hello.html', {'my_name': 'dahee'}) # 위와 똑같은 코드

def lunch(request):
    menu = ['김밥', '국밥', '김치찌개']

    pick = random.choice(menu)

    context = {
        'pick': pick,
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    luck_numbers = random.sample(range(1, 46), 6)

    context = {
        'luck_numbers': luck_numbers,
    }
    
    return render(request, 'lotto.html', context)

def profile(request, username):

    context = {
        'username': username,
    }

    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3
    context = {
        'number': number,
        'result': result,
    }
    
    return render(request, 'cube.html', context)

def articles(request):
    fake = Faker()
    fake_articles = []

    for i in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }

    return render(request, 'articles.html', context)

def ping(request):
    return render(request, 'ping.html')

# ping/에 데이터를 입력하고 제출하면 pong/으로 이동하면서 에러 뜸
# => 에러 밑에 request information : request변수가 갖고있는 정보들
# => request.GET : ping/에서 입력한 데이터, 딕셔너리
def pong(request): 
    # print(request.GET['title'])
    # print(request.GET['content']) # 값이 없을 때 키에러가 발생할 수도 있음

    title = request.GET.get('title')
    content = request.GET.get('content') # 없는 키를 찾거나 값을 입력하지 않으면 None반환

    context = {
        'title': title,
        'content': content,
    }

    return render(request, 'pong.html', context)