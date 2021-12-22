# coding=utf-8
# @Time : 2021/12/22 15:54
# @Author : Karasukaigan
# @File : get_followers.py
# @Software : PyCharm

import requests
import json
import time


def main():
    uid = 433351  # 使用自己的UID可以查询全部粉丝信息，使用他人的UID只能查询前5页粉丝的信息
    response_data = get_followers_data(uid, 1)  # 获取粉丝信息，get_followers_data(uid, 查询页数)
    followers_info = get_followers_info(response_data)  # 只提取出UID和用户名信息
    print(followers_info)
    print_followers_info(followers_info)  # 打印粉丝UID和用户名


# 获取粉丝信息，list_size是粉丝的页数
def get_followers_data(uid, list_size):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "cookie": "",  # 需要自己的cookie
        "referer": "https://space.bilibili.com/"+str(uid)+"/fans/fans",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.131 Safari/537.36"}

    followers_list = []
    for i in range(list_size):
        callback = "__jp" + str(i + 1)
        url = r"https://api.bilibili.com/x/relation/followers?vmid=" + str(uid) + "&pn=" + str(i+1) \
              + "&ps=20&order_type=attention&jsonp=jsonp&callback=" + callback

        try:
            response = requests.get(url, headers=headers)
            r1 = response.text
            r2 = r1.split('(', 1)
            r3 = r2[1].split(')')
            r4 = ''
            for j in range(len(r3)):
                r4 += r3[j]
            response_data = json.loads(r4)
            followers_data = response_data['data']
            followers_list += followers_data['list']
            print("(" + str(i + 1) + "/" + str(list_size) + ")" + str(followers_data['list']))
            time.sleep(1)
        except KeyError:
            print("[KeyError]")
            print(response_data)
            return followers_list

    return followers_list


# 解析数据，获得用户名、UID
def get_followers_info(response_data):
    followers_list = []
    for i in range(len(response_data)):
        followers_list.append({
            'uid': response_data[i]['mid'],
            'name': response_data[i]['uname']
        })
    return followers_list


# 打印粉丝UID和用户名
def print_followers_info(followers_info):
    for i in range(len(followers_info)):
        print("UID：" + '{:<13d}'.format(followers_info[i]['uid']) + "用户名：" + followers_info[i]['name'])


if __name__ == "__main__":
    main()