import jwt
#import consul
import json
import bcrypt
import requests

# from .models import User
from django.views import View
from datetime import datetime
from django.contrib import auth
from rest_framework_jwt.settings import api_settings
from django.shortcuts import render, redirect
from potato.settings import SECRET_KEY
from django.http import HttpResponse, JsonResponse  # HTTP 통신
from django.contrib import messages
from rest_framework import status

# client = consul.Consul(host='172.19.0.100', port=8500)
#
# home = "http://{}:{}/".format(client.catalog.service("main")[1][0]['Address'],
#                               client.catalog.service("main")[1][0]['ServicePort'])
# signin = "http://{}:{}/signin/".format(client.catalog.service("sign")[1][0]['Address'],
#                                        client.catalog.service("sign")[1][0]['ServicePort'])
#
# item_link = "http://{}:{}/items/".format(client.catalog.service("itemDetail")[1][0]['Address'],
#                                          client.catalog.service("itemDetail")[1][0]['ServicePort'])
# user_link = "http://{}:{}/user_detail/".format(client.catalog.service("userDetail")[1][0]['Address'],
#                                                client.catalog.service("userDetail")[1][0]['ServicePort'])

home = 'http://127.0.0.1:8001/'
signin = 'http://127.0.0.1:8002/signin/'
item_link = 'http://127.0.0.1:8003/items/'
user_link = 'http://127.0.0.1:8004/user/'

link = {'home': home, 'signin': signin, 'item_link': item_link, 'user_link': user_link};


def index(request):
    return render(request, 'main/register.html', {'link': link})


def signup(request):
    if request.method == "POST":
        print(request)    
        try:
            
            response = requests.post('http://localhost:8002/userapi/user',data=request.POST)

            print(response.status_code)
            if response.status_code==status.HTTP_400_BAD_REQUEST :
                messages.info(request, '이미 존재하는 Email/nickname입니다.')
                return redirect('./')

            return redirect(link['signin'])

        except KeyError:
            return redirect('./')
     
def get(request):
    userData = User.objects.values()
    return JsonResponse({'member': list(userData)}, status=200)


def loginpage(request):
    return render(request, 'main/login.html', {'link': link})


def login(request):
    # POST 요청이 들어올 경우
    if request.method == "POST":
        try:
            print('hi22')
            response = requests.post('http://localhost:8002/userapi/login',data=request.POST)
            print(response.json())
            if response.status_code == status.HTTP_200_OK :
                token = response.json()['token']
                response = redirect(link['home'], {'TOKEN': token})
                response['TOKEN'] = token
                response.set_cookie('TOKEN', token)
                return response
                    
            else:
                # 예외처리: Password 오류
                messages.info(request, '1.Email 또는 Password가 틀렸습니다.')
                return redirect('./', {'error': 'username or password is incorrect'})
                


        except KeyError:
            messages.info(request, '3.Email 또는 Password가 틀렸습니다.')
            return redirect('./', {'error': 'username or password is incorrect'})

