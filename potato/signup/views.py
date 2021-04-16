
import jwt
import json
import bcrypt

from .models import User
from django.views import View
from datetime import datetime
from django.shortcuts import render, redirect
from potato.settings import SECRET_KEY
from django.http import HttpResponse, JsonResponse #HTTP 통신
from django.contrib import messages


def index(request):
    return render(request,'main/register.html')


def signup(request):
    if request.method == "POST":
        try:
            if User.objects.filter(email= request.POST['email']).exists(): #중복이 되면 안되는 항목
                messages.info(request, '이미 존재하는 Email입니다.')
                return redirect('./')
                # return JsonResponse({'message' : 'Aleady Exist Email'}, status=400)
            elif User.objects.filter(nickname= request.POST['nickname']).exists(): #중복이 되면 안되는 항목
                messages.info(request, '이미 존재하는 Nickname입니다.')
                return redirect('./')
                # return JsonResponse({'message' : 'Aleady nickname Email'}, status=400)
            
            #Email과 nickname이 중복되지 않았을 경우
            User.objects.create(
                email = request.POST['email'],
                password = bcrypt.hashpw(request.POST['password'].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
                nickname = request.POST['nickname'],
                location = request.POST['location'],
                gender = request.POST['gender'],
                birthdate = request.POST['birthdate']
                ).save()
            return redirect('../signin')
            # return HttpResponse(status = 200)

        except KeyError:
            return redirect('./')
            # return JsonResponse({'message' : 'Invalid Key'}, status=400)
        

def get(request):
        userData = User.objects.values()
        return JsonResponse({'member' : list(userData)}, status = 200)