
import jwt
import json
import bcrypt

from .models import User
from django.views import View
from datetime import datetime
from django.contrib import auth
from rest_framework_jwt.settings import api_settings
from django.shortcuts import render, redirect
from potato.settings import SECRET_KEY
from django.http import HttpResponse, JsonResponse #HTTP 통신
from django.contrib import messages

home = 'http://127.0.0.1:8001/'
signin = 'http://127.0.0.1:8002/signin/'
item_link = 'http://127.0.0.1:8003/items/'
link = {'home': home, 'signin': signin, 'item_link': item_link};


def index(request):
    return render(request,'main/register.html', {'link': link})


def signup(request):
    if request.method == "POST":
        try:
            if User.objects.filter(user_email= request.POST['user_email']).exists(): #중복이 되면 안되는 항목
                messages.info(request, '이미 존재하는 Email입니다.')
                return redirect('./')
                # return JsonResponse({'message' : 'Aleady Exist Email'}, status=400)
            elif User.objects.filter(user_nickname= request.POST['user_nickname']).exists(): #중복이 되면 안되는 항목
                messages.info(request, '이미 존재하는 Nickname입니다.')
                return redirect('./')
                # return JsonResponse({'message' : 'Aleady nickname Email'}, status=400)
            
            #Email과 nickname이 중복되지 않았을 경우
            User.objects.create(
                user_email = request.POST['user_email'],
                user_password = bcrypt.hashpw(request.POST['user_password'].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
                user_nickname = request.POST['user_nickname'],
                user_location = request.POST['user_location'],
                user_gender = request.POST['user_gender'],
                user_birthdate = request.POST['user_birthdate']
                ).save()
            return redirect(link['signin'])
            # return HttpResponse(status = 200)

        except KeyError:
            return redirect('./')
            # return JsonResponse({'message' : 'Invalid Key'}, status=400)
        

def get(request):
        userData = User.objects.values()
        return JsonResponse({'member' : list(userData)}, status = 200)


def loginpage(request):
    return render(request, 'main/login.html', {'link': link})


def login(request):
    # POST 요청이 들어올 경우
    if request.method == "POST":
        try:
            # 입력된 Email이 DB에 존재한다면
            # Email이 유효
            if User.objects.filter(user_email=request.POST['user_email']).exists():
                user = User.objects.get(user_email=request.POST['user_email'])
                # 비밀번호(암호화된)를 비교
                # 비밀번호도 유효할 경우
                # 로그인 성공 + 토큰 발급
                if bcrypt.checkpw(request.POST['user_password'].encode("UTF-8"), user.user_password.encode("UTF-8")):
                    token = jwt.encode({'user': user.user_no}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
                    # return JsonResponse({'token': token, 'user':user.id}, status = 200)
                    return redirect(link['home'])
                # 예외처리: Password 오류
                messages.info(request, '1.Email 또는 Password가 틀렸습니다.')
                return redirect('./', {'error': 'username or password is incorrect'})
                # return HttpResponse(status = 401)
            # 예외처리: 존재하지 않는 Email
            messages.info(request, '2.Email 또는 Password가 틀렸습니다.')
            return redirect('./', {'error': 'username or password is incorrect'})
            # return HttpResponse(status= 400)

        except KeyError:
            messages.info(request, '3.Email 또는 Password가 틀렸습니다.')
            return redirect('./', {'error': 'username or password is incorrect'})
            # return render(request, 'signin/', {'error':'username or password is incorrect'})
            # return JsonResponse({'message : Invalid Key'}, status = 400)

