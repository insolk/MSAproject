from django.db import models

#로그인에 필요한 데이터를 저장할 DB 테이블 생성
#Table : my_topic_users
#Kafka를 사용해 회원가입된 User의 데이터를 동기화한다.

#[Kafka를 사용한 이유]
#회원가입은 User의 Data를 Insert하는 용도이고
#로그인은 Select하는 용도이므로
#동일한 데이터에 접근하는 방식에 따라 테이블을 분리하기 위해서 사용
class Login(models.Model):
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
        db_table = 'my_topic_users' #테이블명