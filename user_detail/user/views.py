from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
import os

from django.shortcuts import render, redirect

import jwt
import json
import requests

from mysite.settings import JWT_SECRET_KEY

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


def logout(request):
    response = HttpResponseRedirect(home)
    response.delete_cookie('TOKEN')
    return response

class userDV(DetailView):
    model = User
    template_name = "user/index.html"


    def get_object(self):

        if 'TOKEN' in self.request.COOKIES:
            token = self.request.COOKIES['TOKEN']
            user_no = jwt.decode(token, JWT_SECRET_KEY, algorithm='HS256')
            return self.model.objects.get(pk=user_no['user'])


        else:
            print(signin)
            return redirect('http://www.naver.com')

    def get_context_data(self, **kwargs):
        link = super(userDV, self).get_context_data(**kwargs)
        link['home'] = home
        link['signin'] = signin
        link['item_link'] = item_link
        link['user_link'] = user_link
        if 'TOKEN' in self.request.COOKIES:
            token = self.request.COOKIES['TOKEN']
        else:
            token = ""
        link['token'] = token
        return link
