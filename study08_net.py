# coding=utf-8
import json

import requests

'''
网络编程
需要在pycharm中导入requests   Preference--Projects:xx--Project Interpreter--搜索requests
'''


def request(url):
    r = requests.get(url)
    print(r.text)


request("https://www.baidu.com")

# 拼接URL
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://www.baidu.com/', params=payload)
print(r.url)
# http://www.baidu.com/?key2=value2&key2=value3&key1=value1

# 定制请求头
url = 'https://www.baidu.com/s?wd=python'
headers = {
    'Content-Type': 'text/html;charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
r = requests.get(url, headers=headers)
print(r.url)

'''
post请求
1.最常见post提交数据的方式，以form表单形式提交数据
application/x-www-form-urlencoded
2.以json串提交数据。
application/json
3.一般使用来上传文件
multipart/form-data
'''
payload = {'key1': 'value1',
           'key2': 'value2'
           }
r = requests.post("http://httpbin.org/post", data=payload)
json_data = r.json()
url = json_data.get("url")
print(json_data)
print("resonse返回的json中的url=%s" % url)

# 以json形式发送post请求
url = 'http://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=json.dumps(payload))
