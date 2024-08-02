from urllib.request import urlopen
import requests

url = "https://www.bilibili.com/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}


resp = requests.get(url, headers=headers)

with open ("mybilibili.html", mode="w", encoding= "utf-8") as f:
    f.write(resp.text)