import json
import os
from django.shortcuts import render, redirect
import logging
from django.views.generic import ListView
from .models import Item
from django.views.generic import CreateView
from .forms import ItemForm

logger = logging.getLogger(__name__)


# Create your views here.

class ItemLV(ListView):
    model = Item
    template_name = 'potatomarket/index.html'
    context_object_name = 'items'
    paginate_by = 6


class ItemCreateView(CreateView):
    template_name = 'potatomarket/add_item.html'
    success_url = '/'  # 1
    form_class = ItemForm  # 2

    def form_valid(self, form):
        form.instance.user = self.request.user
        logger.debug("'item_name': {}, 'item_price': {}, 'item_detail': {}".format(self.request.POST.get('item_name'),
                                                                                   self.request.POST.get('item_price'),
                                                                                   self.request.POST.get('item_detail')))
        return super(ItemCreateView, self).form_valid(form)
