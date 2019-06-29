from urllib.request import urlopen
import json
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)

"""Example1:"""
# # 读取数据
# req = response.read()
# # 将数据写入文件
# with open('btc_close_2017.json','wb') as f:
# 	f.write(req)
# # 加载json格式
# file_urllib = json.loads(req)
# print(file_urllib)

"""Example2"""
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017.json', 'w') as f:
	f.write(req.text)
file_requests = req.json()