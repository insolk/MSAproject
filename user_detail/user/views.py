from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
import os

from django.shortcuts import render,redirect

import jwt
import json
import requests


from mysite.settings import JWT_SECRET_KEY     

signin = 'http://127.0.0.1:8002/signin/'

class userDV(DetailView):
    model = User
    template_name = "user/index.html"


    def get_object(self):

        if 'TOKEN' in self.request.COOKIES:
            token = self.request.COOKIES['TOKEN']
            user_no = jwt.decode(token,JWT_SECRET_KEY,algorithm='HS256')
            print(user_no)
            print(user_no['user'])
            print(self.request.COOKIES)
            return self.model.objects.get(pk=user_no['user'])
            

        else:
            print(signin)
        
            return redirect('http://www.naver.com')



