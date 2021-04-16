from django.db import models

class user(models.Model):
    user_no = models.IntegerField(primary_key=True)
    user_pwd = models.CharField(max_length=100)
    user_email = models.CharField(max_length=50)
    user_location = models.CharField(max_length=20)
    user_gender = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=20)
    user_created = models.DateTimeField('Create Date', auto_now_add=True)
    user_birthdate = models.DateTimeField(max_length=9) # char? date?
    user_caution = models.IntegerField(blank=True, null=True) 
    user_sell_count = models.IntegerField(blank=True, null=True)

    class Meta:
         db_table = 'user'
