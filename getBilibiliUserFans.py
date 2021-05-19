# coding=utf-8
# @Time : 2021/5/19 16:03
# @Author : Karasukaigan
# @File : getBilibiliUserFans.py
# @Software : PyCharm


import requests
import json


def main():
    uid = 433351  # 某只鹅的UID
    responseData = getUserData(uid)  # 该函数返回一个包含用户信息的字典
    userData = responseData['data']  # 用户数据，包含信息卡、粉丝量等信息
    userCard = userData['card']  # 用户信息卡，包含用户ID（昵称）、签名等信息

    print("B站ID：" + userCard['name'])
    print("粉丝数：" + str(userData['follower']))


def getUserData(uid):
    url = r"https://api.bilibili.com/x/web-interface/card?jsonp=jsonp&mid=" + str(uid)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36", }

    response = requests.get(url, headers=headers)

    return json.loads(response.text)


if __name__ == "__main__":
    main()
