# coding=utf-8
# @Time : 2021/12/22 2:03
# @Author : Karasukaigan
# @File : get_live_info.py
# @Software : PyCharm

import requests
import json
import get_user_info


def main():
    # 房间号
    # EdmundDZhang:5050
    # 神奇陆夫人:115

    room_id = 5050  # 某只鹅的直播间ID
    response_data = get_live_data(room_id)  # 该函数返回一个包含直播间信息的字典
    uid = get_uid(response_data)  # 获取主播UID
    response_data_user = get_user_info.get_user_data(uid)  # 获取主播用户信息

    print("房间号：" + str(get_room_id(response_data)))
    print("B站用户名：" + get_user_info.get_name(response_data_user))
    print("UID：" + str(get_uid(response_data)))
    print("被隐藏：" + str(is_hidden(response_data)))
    print("被封禁：" + str(is_locked(response_data)))
    print("手机直播：" + str(is_portrait(response_data)))
    print("直播状态：" + get_live_status(response_data))
    print("直播间地址：" + "https://live.bilibili.com/" + str(room_id))
    # print(get_all_info(response_data))


def get_live_data(room_id):
    url = r"https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id=" + str(room_id) + "&protocol=0,1&format=0,1,2&codec=0,1&qn=0&platform=web&ptype=8"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.131 Safari/537.36"}

    response = requests.get(url, headers=headers)
    return json.loads(response.text)


# 获取所有数据
def get_all_info(response_data):
    user_data = response_data['data']
    return user_data


# 获取房间号
def get_room_id(response_data):
    user_data = response_data['data']
    return user_data['room_id']


# 获取UID
def get_uid(response_data):
    user_data = response_data['data']
    return user_data['uid']


# 是否被隐藏
def is_hidden(response_data):
    user_data = response_data['data']
    return user_data['is_hidden']


# 是否被封禁
def is_locked(response_data):
    user_data = response_data['data']
    return user_data['is_locked']


# 是否为手机直播
def is_portrait(response_data):
    user_data = response_data['data']
    return user_data['is_portrait']


# 获取直播状态，0是未开播，1是直播，2是轮播
def get_live_status(response_data):
    user_data = response_data['data']
    if user_data['live_status'] == 0:
        return "未开播"
    elif user_data['live_status'] == 2:
        return "轮播"
    else:
        return "已开播"


if __name__ == "__main__":
    main()