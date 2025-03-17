# Django

## 0. Setting

- `.gitignore` : 필요없는 파일 처리(python, windows, macOS, django)
- `python -m venv venv` : 가상환경 설정
    - `source venv/Script/activate` : 가상환경 활성화
- `README.md` : 작성 습관화 하기
- `pip install faker` : faker 라이브러리 설치 
    - [faker](https://pypi.org/project/Faker/)

## 1. Django 프로젝트
1. Django 설치
```shell 
# shell : 터미널에 사용하는 문법
pip install django # 가상환경 활성화 된 상태에서 설치
```

2. 프로젝트 생성
```shell
django-admin startproject <pjt-name> <path>
```
-  ` django-admin startproject first_pjt .`
    - django가 설치된 상태에서 이름이 first_pjt인 프로젝트를 현재 위치에서 시작 => first_pjt 폴더(5개의 파일)와 manage.py파일을 만들어줌
    - manage.py : 터미널창에서 장고한테 명령어를 내릴 떄 사용하는 파일
    - mysit/ : 프로젝트 폴더(지금은 first_pjt)
        - `__init__.py` : 모듈로 동작할 수 있도록 만들어주는 파일
        - `settings.py` : 각종 장고 설정(시간, 데이터베이스)
        - `urls.py` : 어떤 요청이 들어왔을 떄 views.py안의 데이터와 연결
        - `asgi.py`
        - `wsgi.py`

3. 서버 실행 (종료 : `ctrl + c`)
```shell
python manage.py runserver
```
- 서버가 계속 돌아가고있음 : 내가 해당하는 주소로 누가 불러줄 때까지 계속 기다림
- http://127.0.0.1:8000/
    - 127.0.0.1 : 내 컴퓨터에서 돌아가는 주소
    - 8000 : 포트(개발서버들은 보통 8000 포트, http는 80포트, https는 443포트 사용)

4. 앱 생성
```shell
django-admin startapp <app-name> # 경로설정 안하면 현재 폴더에 자동으로 생성
# python manage.py startapp <app-name> => 위와 같은 코드
```
- `django-admin startapp first_app` : 앱 폴더(first_app) 생성

5. 앱 등록(`first_pjt/settings.py`에서 등록)
```python
INSTALLED_APPS = [
    ...,
    '<app-name>',
]
```
- 'settings.py'파일의 INSTALLED_APPS에 'first_app' 등록

![](MTV.png)

1. `urls.py` : 어떤 경로를 받을지 설정, 실행하고싶은 기능의 영어철자를 사용하는게 일반적 => 보자마자 url이 어떤 기능을 할지 예측 가능해야함
2. `views.py` : 실행시키고싶은 함수를 모아놓은 파일 => 함수의 이름은 경로 이름과 같게 설정
3. `.html` : 사용자가 보는 형태를 적은 파일
    - tab(자동완성)이 안되면 우측 하단에 html로 되어있는지 확인 => django로 되어있으면 html로 바꿔야함

- 경로설정 (`urls.py`)
```python
`from first_app import view` : first_app 폴더 내부의 view.py 파일 가져오기
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```
- 기능 구현(`views.py`)
```python
def index(request):
    return render(request, 'index.html')
```
- `first_app`폴더 안에 `templates` 폴더 만들기
- `templates` 폴더 안에 `index.html` 파일 만들기
```html
<!--`! + tab`누른 후 <body>에 <h1>hello</h1> 추가-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>hello!</h1>
</body>
</html>
```

- html은 정적인 파일
- 동적으로 만들기
    - `views.py`파일 안의 함수 안에 `context={키:값,}`만들고 `return render()`에 인자로 `context`추가
    - `.html`파일의 <body>안에 {{딕셔너리 키값}}을 포함하는 태그 작성
    - {{context의 키}} : django안의 render()가 만들어주는 함수

- 경로설정 변수화(variable routing)
    - `urls.py` 파일에 `path('profile/<username>/', views.profile)`
        - 숫자를 받는 경우 : `<int:number>` => `views.py`에서 int(number)로 선언해줄 수 있지만 문자를 넣었을 떄 다른 오류가 생김
    - `views.py` 파일에 함수를 선언할 때 username을 인자로 설정 : `def profile(request, username):`

- html파일에서 python 코드 쓰기
```html
<body>
    {%for a in b%}
        <p> {{a}} </p>
    {% endfor %} <!-- for문을 끝냄 -->
</body>
```
    - html파일에 주석에 {%%}을 포함하면면 주석처리된 것처럼 보이지만 django는 읽으려고 시도함
    - django에서 주석다는 방법
```django
{%comment%}

{%endcomment%}
```