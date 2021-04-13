from django.db import models

# Create your models here.
# Create your models here.
class User(models.Model):
    objects = models.Manager()
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    # nickname = models.CharField(max_length=100, unique=True)
    # birthdate = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'users' #테이블명