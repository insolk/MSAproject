import jwt
import json
import bcrypt

from .models import Login
from django.views import View
from django.contrib import auth
from potato.settings import SECRET_KEY
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework_jwt.settings import api_settings
from django.http import HttpResponse, JsonResponse #HTTP 통신
from django.contrib import messages

def index(request):
    return render(request,'main/login.html')
    
def login(request):
    #POST 요청이 들어올 경우
    if request.method == "POST":
            try:
                #입력된 Email이 DB에 존재한다면
                #Email이 유효
                if Login.objects.filter(email=request.POST['email']).exists(): 
                    user = Login.objects.get(email = request.POST['email'])    
                    #비밀번호(암호화된)를 비교
                    #비밀번호도 유효할 경우
                    #로그인 성공 + 토큰 발급
                    if bcrypt.checkpw(request.POST['password'].encode("UTF-8"), user.password.encode("UTF-8")):
                        token = jwt.encode({'user' : user.id}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
                        # return JsonResponse({'token': token, 'user':user.id}, status = 200)
                        return redirect('../')
                    #예외처리: Password 오류
                    messages.info(request, '1.Email 또는 Password가 틀렸습니다.')
                    return redirect('./', {'error':'username or password is incorrect'})
                    # return HttpResponse(status = 401)
                #예외처리: 존재하지 않는 Email
                messages.info(request, '2.Email 또는 Password가 틀렸습니다.')
                return redirect('./', {'error':'username or password is incorrect'})
                # return HttpResponse(status= 400)

            except KeyError:
                messages.info(request, '3.Email 또는 Password가 틀렸습니다.')
                return redirect('./', {'error':'username or password is incorrect'})
                # return render(request, 'signin/', {'error':'username or password is incorrect'})
                # return JsonResponse({'message : Invalid Key'}, status = 400)

