# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .exceptions import RegUserError

import hashlib
import time

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    nickname = models.CharField(max_length=100, null=False)
    status = models.IntegerField(default=0)
    ctime = models.DateField(auto_now_add=True)

    @classmethod
    def encry_password(cls, password):
        if password:
            _md5 = hashlib.md5()
            _md5.update(password)
            return _md5.hexdigest()
        else:
            return password

    def set_password(self, password):
        self.password = User.encry_password(password)
        return self.password

    def check_password(self, password):
        return self.password == User.encry_password(password)
    
    @classmethod
    def generate_nickname(cls, pre=''):
        nickname = '匿名用户%s%d' % (pre, int(time.time()*100000))
        return nickname
    
    class Meta:
        db_table = 'mytime_user'


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    creator = models.IntegerField(null=False)
    eventTime = models.DateTimeField(null=False)
    content = models.CharField(max_length=2000, default='')
    ctime = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mytime_task'

class UserTimeLine(models.Model):
    owner = models.IntegerField(null=False)
    timeline = models.IntegerField(null=False)
    spendtime = models.IntegerField(null=False)
    taskid = models.IntegerField(null=False)
    ctime = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mytime_usertimeline'


class UserService(object):
    def query_by_username(self, username):
        user = None
        if username:
            try:
                user = User.objects.get(username = username)
            except Exception as err:
                print("Error:UserService.query_by_username(%s)=>" % username, err)
        return user

    def reg_user(self, username, password, nickname):
        if not nickname:
            nickname = User.generate_nickname()
        result = 0
        user = User(username = username, password = password, nickname = nickname)
        try:
            user.save()
            result = 1
        except Exception as err:
            print("Error:reg_user(%s, %s, %s)" % (username, password, nickname), err)
        return result


    
userService = UserService()