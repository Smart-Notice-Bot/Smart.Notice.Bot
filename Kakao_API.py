#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send
# 나에게 보내는 방법입니다.

# Bearer뒤에 공백포함 + 자신의 access Token 을 붙여줍니다.
headers={
    "Authorization" : "Bearer " + 사용자 access Token
}

#text에 전송하고자 할 문구를 넣습니다.
data={
    "template_object": json.dumps({
        "object_type":"check send message",
        "text":"Please",
        "link":{
            "web_url":"www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code


# In[3]:


#친구에게 보내기 방법입니다. 우선 친구목록을 불러옵니다.
#카카오 Developer 친구 목록
friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

#Header에도 똑같은 방식으로 정의해줍니다.
headers={"Authorization" : "Bearer " + 사용자 access Token}

result = json.loads(requests.get(friend_url, headers=headers).text)

print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
# print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id) #친구 목록 확인


# In[6]:


def getFriendsList(): #친구목록 함수를 이용해 불러오기 2번째 방법입니다. 
    header = {"Authorization": 'Bearer ' + 사용자 access Token}
    url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 정보 요청

    result = json.loads(requests.get(url, headers=header).text)

    friends_list = result.get("elements")
    friends_id = []

    print(requests.get(url, headers=header).text)
    print(friends_list)

    for friend in friends_list:
        friends_id.append(str(friend.get("uuid")))

        return friends_id


# In[7]:


getFriendsList() #함수호출


# In[8]:


#친구에게 카카오톡 메세지 보내기

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

#똑같이 정의
headers={"Authorization" : "Bearer " + 사용자 access Token}

result = json.loads(requests.get(friend_url, headers=headers).text)

print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
# print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id)

send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

#보내는 메세지 data 변수
#보내고자 하는 문구는 text에 넣으면 됩니다.
data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"성공입니다!",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code





