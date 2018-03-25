# -*- coding: utf-8 -*-

class RegUserError(Exception):
    def __init__(self, tip=''):
        self.tip = tip
    
    def __str__(self):
        return '注册用户错误!%s' % self.tip