from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from search.forms import SearchForm
from search.es import search_category

import os
from random import randint

def search(request):
    result=[]
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            category = form.cleaned_data['category']
            search_keyword = form.cleaned_data['search_keyword']

            if category:
               result = search_category(category,search_keyword)
                

        
        return render(request, 'search/search.html', {'result':result})
    else:
        form = SearchForm()
    return render(request, 'search/search.html')

