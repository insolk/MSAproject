import json
import os

from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Item


# Create your views here.

class ItemLV(ListView):
    model = Item
    template_name = 'potatomarket/index.html'
    context_object_name = 'items'
    paginate_by = 10


def item_home(request):
    model = Item.objects.all()
    # current_path = os.getcwd()
    # os.chdir("itscraper")
    # os.system("del ITnews.json")
    # ITCrawling.objects.all().delete()
    # os.system("scrapy crawl itbots")
    # os.chdir(current_path)
    #
    # with open('itscraper/ITnews.json', "r", encoding="utf-8") as json_file:
    #     json_data = json.load(json_file)
    #
    # for item in json_data:
    #     data = ITCrawling.objects.create(title=item.get('title'),
    #                                      theme=item.get('theme'),
    #                                      description=item.get('description'),
    #                                      author=item.get('author'),
    #                                      url=item.get('url'), )
    # return redirect('crawling:it_index')

    # return render(request, 'crawling/IT_news.html', {'news': model})

