#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import yagmail
import random
import time
import os
import json

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

# glados 签到 url
url = "https://glados.rocks/api/user/checkin"
cookies = {
    "koa:sess": "eyJ1c2VySWQiOjM0NjY0LCJfZXhwaXJlIjoxNzE2NDMyOTU5NTQ1LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=",
    "koa:sess.sig": "plDXcVXj0oMuDf35QAgs6Oyj_gs",
    "__stripe_mid": "eacc2440-5c4f-4368-ab1f-5b961f8e7a0bbdcaad",
    "_ga_CZFVKMNT9J": "GS1.1.1690512957.9.1.1690513362.0.0.0",
    "_ga": "GA1.1.1156446483.1676172823"
}
# from 请求负载
value = {"token": "glados.network"}

# wait some times
time.sleep(random.randint(30, 300))

result = requests.post(url, cookies=cookies, data=value)
result_json = result.json()

print(result_json)

code = result_json['code']
message = result_json['message']

msg = {
    "status": code,
    "message": message
}

#print(msg)

# password 是 qq 的密码框(需要开启服务)
yag = yagmail.SMTP(user=email, password=password, host='smtp.qq.com')
yag.send(to=email, subject='glados sign in', contents=msg)
