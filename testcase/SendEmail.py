#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import requests

"""
发送邮件
"""
def SendEmail():

    host_server = "smtp.exmail.qq.com"
    sender_addr = "zhenqing.cai@argrace.ai"
    pwd = "csdkgZ5GpyyeogmL"
    receiver = ["zhenqing.cai@argrace.ai"]
    email_title = "Test Sending Email"
    email_content = "this is just a test email, please ignore it"


    #初始化邮件主体
    message = MIMEMultipart()
    message["Subject"] = email_title
    message["From"]  = sender_addr
    #message["To"] = Header("测试邮件","utf-8")
    message["To"] = ";".join(receiver)
    message.attach(MIMEText(email_content,"plain","utf-8"))


    smpt = SMTP_SSL(host = host_server)
    smpt.login(sender_addr, pwd)
    smpt.sendmail(sender_addr, receiver,message.as_string())

    smpt.quit()


def getToken():

    header = {
            "Accept":"application/json, text/plain, */*",
            "Content-Type":	"application/x-www-form-urlencoded",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36"
            }
    url = "http://139.224.193.77:9006/backapi/admin/login"
    params = {"user_name":13535201163 ,"password":"z82BInnQyu4wI7meRPqsOH8sC1KkEJ3yE1MCliPl15hSz+c+EIx0mAanyY6/NIBSfcisgBlkLB6t6r4JW9solh6V8m/WpbRtSHDx2VuYWJO2qQnBxBkUKtY85dTokbx9xE+XSSPJs86yU88wQtGJ94yMtRN5YuIfQCKaPKK4JRc=",
              "lang":"zh_CN"}
    response = requests.post(url= url, data=params, headers= header).json()

    token= response["companies"][0]["token"]

    return token

def checkDeviceStatus(Id,deviceId):

    header={
        "User-Agent" :  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36",
        "Accept":"application / json, text / plain, * / *",
        "authorization": "Bearer "+getToken()
    }
    startTime= int(time.time()-120)*1000  #2分钟前


    url = "http://139.224.193.77:9006/devices/{}/message?locale=zh_CN&startTime={}&type=0&device_id={}&lang=zh_C"\
        .format(Id,startTime,deviceId)
    params= {"locale":"zh_CN","startTime":"1643299200000","type":"0","device_id":"MQTT_001","lang":"zh_C"}

    response = requests.get(url= url,data = params, headers =header).json()

    print(response)

def timesss():

    print(int(time.time()-120)*1000)
    print(time.localtime(time.time()))
    print(time.localtime())


if __name__ == "__main__" :

    devicesId = {"MQTT_001":"208494",
                 "MQTT_002":"208500",
                 "MQTT_003":"208503",
                 "MQTT_004":"215704"}

    for k,v in devicesId.items():

        checkResult= checkDeviceStatus(v,k)


