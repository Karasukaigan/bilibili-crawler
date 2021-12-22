# coding=utf-8
# @Time : 2021/12/21 22:58
# @Author : Karasukaigan
# @File : get_user_info.py
# @Software : PyCharm

import requests
import json
import get_live_info


def main():
    uid = 433351  # 某只鹅的UID
    response_data = get_user_data(uid)  # 该函数返回一个包含用户信息的字典
    room_id = get_live_roomid(response_data)
    response_data_live = get_live_info.get_live_data(room_id)  # 获取直播间信息

    print("B站用户名：" + get_name(response_data))
    print("MID：" + str(get_mid(response_data)))
    print("性别：" + get_sex(response_data))
    print("头像URL：" + get_face(response_data))
    print("用户等级：" + str(get_level(response_data)))
    print("关注数：" + str(get_attention(response_data)))
    print("粉丝数：" + str(get_fans(response_data)))
    print("获赞数：" + str(get_like_num(response_data)))
    print("签名：" + get_sign(response_data))
    print("房间号：" + str(get_live_roomid(response_data)))
    print("直播间地址：" + get_live_room_url(response_data))
    print("直播状态：" + get_live_info.get_live_status(response_data_live))
    # print(get_all_info(response_data))


# 提取所有有用信息
def get_all_info(response_data):
    result = {
        'name': get_name(response_data),
        'mid': get_mid(response_data),
        'sex': get_sex(response_data),
        'face': get_face(response_data),
        'level_info': get_level(response_data),
        'attention': get_attention(response_data),
        'fans': get_fans(response_data),
        'like_num': get_like_num(response_data),
        'sign': get_sign(response_data),
        'roomid': get_live_roomid(response_data),
        'live_room_url': get_live_room_url(response_data)
    }
    return result


# 请求用户数据
def get_user_data(uid):
    url1 = r"https://api.bilibili.com/x/web-interface/card?jsonp=jsonp&mid=" + str(uid)
    url2 = r"https://api.bilibili.com/x/space/acc/info?mid=" + str(uid) + "&jsonp=jsonp"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36"}

    response1 = requests.get(url1, headers=headers)
    response_data1 = json.loads(response1.text)
    user_data1 = response_data1['data']
    response2 = requests.get(url2, headers=headers)
    response_data2 = json.loads(response2.text)
    user_data2 = response_data2['data']
    response_data = {**user_data1, **user_data2}
    return response_data


# 获取用户名
def get_name(response_data):
    return response_data['name']


# 获取用户MID（UID）
def get_mid(response_data):
    return response_data['mid']


# 获取用户性别
def get_sex(response_data):
    return response_data['sex']


# 获取用户头像URL
def get_face(response_data):
    return response_data['face']


# 获取粉丝数
def get_fans(response_data):
    return response_data['follower']


# 获取获赞数
def get_like_num(response_data):
    return response_data['like_num']


# 获取关注数
def get_attention(response_data):
    user_card = response_data['card']
    return user_card['attention']


# 获取签名
def get_sign(response_data):
    return response_data['sign']


# 获取用户等级
def get_level(response_data):
    return response_data['level']


# 获取直播间地址
def get_live_room_url(response_data):
    live_room = response_data['live_room']
    return live_room['url']


# 获取直播间房间号
def get_live_roomid(response_data):
    live_room = response_data['live_room']
    return live_room['roomid']


if __name__ == "__main__":
    main()
