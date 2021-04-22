# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comment(models.Model):
    comment_no = models.AutoField(primary_key=True)
    item_no = models.ForeignKey('Item', models.DO_NOTHING, db_column='item_no')
    comment_modify_date = models.DateTimeField(blank=True, null=True)
    comment_create_date = models.DateTimeField(blank=True, null=True)
    comment_content = models.CharField(max_length=100)
    comment_nickname = models.CharField(db_column='comment_nickName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class Item(models.Model):
    item_no = models.AutoField(primary_key=True)
    user_no = models.IntegerField()
    item_title = models.CharField(max_length=100)
    item_views = models.IntegerField(blank=True, null=True)
    item_price = models.IntegerField()
    item_detail = models.TextField()
    item_img = models.CharField(max_length=100, blank=True, null=True)
    item_status = models.CharField(max_length=10, blank=True, null=True)
    item_soldtime = models.DateTimeField(blank=True, null=True)
    item_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class SoldItem(models.Model):
    item_no = models.AutoField(primary_key=True)
    user_no = models.IntegerField()
    item_title = models.CharField(max_length=100)
    item_views = models.IntegerField()
    item_price = models.IntegerField()
    item_detail = models.TextField()
    item_soldtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sold_item'


class User(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_password = models.CharField(max_length=100)
    user_email = models.CharField(max_length=50)
    user_nickname = models.CharField(max_length=20)
    user_location = models.CharField(max_length=20)
    user_gender = models.CharField(max_length=20)
    user_birthdate = models.DateField(blank=True, null=True)
    user_createat = models.DateField(blank=True, null=True)
    user_caution = models.IntegerField(blank=True, null=True)
    user_sellcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
