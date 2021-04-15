import json
import os

from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Item
from django.views.generic import CreateView
from .forms import ItemForm

# Create your views here.

class ItemLV(ListView):
    model = Item
    template_name = 'potatomarket/index.html'
    context_object_name = 'items'
    paginate_by = 10


class ItemCreateView(CreateView):
    template_name = 'potatomarket/add_item.html'
    success_url = '/' #1
    form_class = ItemForm #2
