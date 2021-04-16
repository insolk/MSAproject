from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
import os
from django.db.models import Q
from django.shortcuts import render

class userDV(DetailView):
    model = user
    template_name = "user/index.html"
    # context_object_name='user'

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data()
    #     return context


