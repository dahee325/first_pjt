import random # 파이썬이 기본으로 가지고있는 라이브러리(설치할 필요X)를 위에 씀
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