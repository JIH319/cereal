python -m venv venv



source venv/Scripts/activate



pip list



pip install django django_extensions



pip list

touch README.md  .gitignore



code .

---

가상환경 인터프리터 설정

리드미와 깃이그노어 채우기



git init

git add .

git commit -m 'first commit'

---

* 프로젝트 실수 했을 때 >> rm -rf (지울것)
* pip freeze > requirements.txt : 관리(협업 대비)





django-admin startproject (프로젝트이름)

python manage.py runserver : 확인 가능



설정관련 :  setting >> LANGUAGE, TIME // 앱이름은 만들기전에 적지말것!

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

---

python manage.py startapp (앱이름)

설정관련 :  setting >> INSTALLED APP// 앱이름은 만들기전에 적지말것!

---

## 1. models.py

제일 먼저 어떻게 정의할지, 어떤 데이터를 다룰지 정해야함 



python manage.py makemigrations

python manage.py migrate

---

## 2. admin.py

python manage.py createsuperuser

