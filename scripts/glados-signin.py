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
    "koa:sess": "eyJ1c2VySWQiOjM0NjY0LCJfZXhwaXJlIjoxNzAyNTIzNjU3Njk3LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=",
    "koa:sess.sig": "6CQ_cZ_CC_uaAVIoVQvwb-7nKjA",
    "__stripe_mid": "b722e623-8452-4092-996e-3fe9533bcc2bfdb53b",
    "_gid": "GA1.2.2108941348.1677120628",
    "_ga": "GA1.2.1838872950.1675740084",
    "_gat_gtag_UA_104464600_2": "1",
    "_ga_CZFVKMNT9J": "GS1.1.1677135491.7.0.1677135496.0.0.0"
}
# from 请求负载
value = {"token": "glados.network"}

# wait some times
time.sleep(random.randint(30, 300))

result = requests.post(url, cookies=cookies, data=value)
result_json = result.json()

# print(result_json)

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
