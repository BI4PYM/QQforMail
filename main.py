#!python3
# -*- coding:utf-8 -*-
import os
import sys
import time
import uiautomation as auto
# thanks for yinkaisheng's uiautomation.URL https://github.com/yinkaisheng/Python-UIAutomation-for-Windows
import smtplib
from email.mime.text import MIMEText
mail_host = 'smtp.mail.com'  
mail_user = 'user'   
mail_pass = 'password'   
sender = 'abc@mail.com'  
receivers = ['xyz@mail.com']  

ItemsList = []
AllList=[]

def GetPersonDetail():
    detailWindow = auto.WindowControl(searchDepth= 1, ClassName = 'TXGuiFoundation', SubName = '的资料')
    details = ''
    for control, depth in auto.WalkControl(detailWindow):
        if isinstance(control, auto.EditControl):
            details += control.Name + control.GetValuePattern().Value + '\n'
    details += '\n' * 2
    detailWindow.Click(-10, 10)
    return details


def GetAllItems():
    AllList = auto.GetRootControl().split('\n')
    for n in range(len(AllList)):
        if str(AllList(n)).find('ListItemControl') != -1:
            ItemsList = ItemsList + AllList(n)

def 
