from django.shortcuts import render
from django.contrib import auth
import json
from .models import User
from django.views import View
from django.http import HttpResponse, JsonResponse #HTTP 통신
# Create your views here.

def index(request):
    return render(request,'main/signin.html')

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])

                if user.password == data['password']:
                    return HttpResponse(status = 200)
                return HttpResponse(status = 401)
            return HttpResponse(status= 400)

        except KeyError:
            return JsonResponse({'message : Invalid Key'}, status = 400)