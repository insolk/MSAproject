from django.db import models

#회원가입시 입력된 데이터를 저장한 테이블
#Table:  users
class User(models.Model):
    objects = models.Manager()
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthdate = models.DateField(null=False)
    createat = models.DateField(auto_now_add=True)
    caution = models.IntegerField(default=0)
    sellcount = models.IntegerField(default=0)

    class Meta:
        db_table = 'users' #테이블명