import requests

url = "https://www.zhipin.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers, timeout=10)
print("状态码:", resp.status_code)
print("页面标题:", resp.text[resp.text.find("<title>") + 7 : resp.text.find("</title>")])
