from django.shortcuts import render
import json
import bcrypt
import jwt
from potato.settings import SECRET_KEY
from .models import User
from django.views import View
from django.http import HttpResponse, JsonResponse #HTTP 통신
# Create your views here.

def index(request):
    return render(request,'main/signup.html')


class SignupView(View):
    def post(self,request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email= data['email']).exists():
                return JsonResponse({'message' : 'Aleady Exist Email'}, status=400)
        
            User.objects.create(
                email = data['email'],
                password = bcrypt.hashpw(data['password'].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")).save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({'message' : 'Invalid Key'}, status=400)

    def get(self,request):
        userData = User.objects.values()
        return JsonResponse({'member' : list(userData)}, status = 200)

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode("UTF-8"), user.password.encode("UTF-8")):
                    token = jwt.encode({'user' : user.id}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
                    return JsonResponse({'token': token}, status = 200)
                return HttpResponse(status = 401)
            return HttpResponse(status= 400)

        except KeyError:
            return JsonResponse({'message : Invalid Key'}, status = 400)