# coding=utf-8
# @Time : 2021/12/21 22:58
# @Author : Karasukaigan
# @File : get_user_info.py
# @Software : PyCharm

import requests
import json


def main():
    uid = 433351  # 某只鹅的UID
    response_data = get_user_data(uid)  # 该函数返回一个包含用户信息的字典

    print("B站用户名：" + get_name(response_data))
    print("MID：" + get_mid(response_data))
    print("性别：" + get_sex(response_data))
    print("头像URL：" + get_face(response_data))
    print("用户等级：" + str(get_level_info(response_data)))
    print("关注数：" + str(get_attention(response_data)))
    print("粉丝数：" + str(get_fans(response_data)))
    print("获赞数：" + str(get_like_num(response_data)))
    print("签名：" + get_sign(response_data))
    # print(get_all_info(uid))


def get_all_info(uid):
    response_data = get_user_data(uid)
    result = {
        'name': get_name(response_data),
        'mid': get_mid(response_data),
        'sex': get_sex(response_data),
        'face': get_face(response_data),
        'level_info': get_level_info(response_data),
        'attention': get_attention(response_data),
        'fans': get_fans(response_data),
        'like_num': get_like_num(response_data),
        'sign': get_sign(response_data)
    }
    return result


def get_user_data(uid):
    url = r"https://api.bilibili.com/x/web-interface/card?jsonp=jsonp&mid=" + str(uid)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36"}

    response = requests.get(url, headers=headers)
    return json.loads(response.text)


# 获取用户名
def get_name(response_data):
    user_data = response_data['data']  # 用户数据，包含信息卡、粉丝量等信息
    user_card = user_data['card']  # 用户信息卡，包含用户ID（昵称）、签名等信息
    return user_card['name']


# 获取用户MID
def get_mid(response_data):
    user_data = response_data['data']
    user_card = user_data['card']
    return user_card['mid']


# 获取用户性别
def get_sex(response_data):
    user_data = response_data['data']
    user_card = user_data['card']
    return user_card['sex']


# 获取用户头像URL
def get_face(response_data):
    user_data = response_data['data']
    user_card = user_data['card']
    return user_card['face']


# 获取粉丝数
def get_fans(response_data):
    user_data = response_data['data']
    return user_data['follower']


# 获取获赞数
def get_like_num(response_data):
    user_data = response_data['data']
    return user_data['like_num']


# 获取关注数
def get_attention(response_data):
    user_data = response_data['data']
    user_card = user_data['card']
    return user_card['attention']


# 获取签名
def get_sign(response_data):
    user_data = response_data['data']
    user_card = user_data['card']
    return user_card['sign']


# 获取用户等级
def get_level_info(response_data):
    user_data = response_data['data']
    user_card = user_data['card']
    user_level_info = user_card['level_info']
    return user_level_info['current_level']


if __name__ == "__main__":
    main()
