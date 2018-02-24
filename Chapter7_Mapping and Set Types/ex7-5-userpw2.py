#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''简单的用户管理系统'''

import base64,hashlib
from datetime import datetime
import getpass
import time

inittime = datetime.now()
db = {'admin': ['21232f297a57a5a743894a0e4a801fc3', inittime]}

def newuser(name):
        value=[]
        while True:
                if  not name.isalnum() and '' in name:
                        print '错误！请输入仅包含数字和字母组成的账号名!'
                        continue
                else:
                        if db.has_key(name):
                                print '账号已存在，请重新输入!'
                                continue
                        else:
                                break
        pwd = getpass.getpass()
        m=hashlib.md5()
        m.update(pwd)
        value.append(m.hexdigest())
        value.append(datetime.now())
        db[name] = value
        print '新账号已生成:%s【%s】' %(name,value[1])

def olduser(name):
#       name = raw_input('login: ').lower()
        pwd = getpass.getpass('passwd: ')
        m = hashlib.md5()
        m.update(pwd)
        passwd = db.get(name)
        if passwd[0] == m.hexdigest():
                newtime = datetime.now()
                if (newtime-db[name][1]).days==0 and (newtime-db[name][1]).seconds<14400:
                        print '你已经于【%s】登录，4小时内内请勿重复登录！' %passwd[1]
                else:
                        passwd[1] = newtime
                        print '欢迎回来!%s 【%s】' %(name,passwd[1])
        else:
                print '账号或密码输入错误!'


def userlogin():
        while True:
                name = raw_input('请输入账号: ').lower()
                if not name.isalnum() and '' in name:
                        print '错误！请输入仅包含数字和字母组成的账号名!'
                        continue
                else:
                        if not db.has_key(name):
                                temp = raw_input('账号不存在，是否创建新账号?(Y/N)').lower()
                                if temp == 'y':
                                        newuser(name)
                                        break
                                elif temp == 'n':
                                        break
                                else:
                                        print '输入错误，请选择Y或N！'
                        else:
                                olduser(name)
                                break


def deluser():
        name = raw_input('输入你想删除的账号:').lower()
        if name in db:
                db.pop(name)
        else:
                print '账号输入错误！'

def showuser():
        for name in db:
                print "账号:%s\n密码:%s\n时间:%s\n" %(name, db[name][0],db[name][1])




def showmenu():
        print '''
#############################################
#                                           #
# Welcome to the login interface!           #
# Powered by Xiaojie Zhou                   #
# Copyright©2018.2.24 All Rights Reserved   #
#                                           #
#############################################'''

        prompt = """
(L)ogin now-------账号登录
(D)elet user------删除账号
(S)how all user---查询账号
(Q)uit------------退出

Enter Chioce: """

        done = False
        while not done:

                chosen = False
                while not chosen:
                        print ''
                        for i in range(1,2):
                                print '主界面等待中...%ss' %i
                                time.sleep(1)
                        try:
                                choice = raw_input(prompt).strip()[0].lower()
                        except (EOFError, KeyboardInterrupt):
                                choice = 'q'
                        print '\n您的选项是: [%s]' % choice
                        if choice not in 'ldsq':
                                print '错误的选项，请重试！'
                        else:
                                chosen = True

                if choice == 'q':done = True
                if choice == 'l':userlogin()
                if choice == 'd':deluser()
                if choice == 's':showuser()

if __name__ == '__main__':
        showmenu()
