import requests

url="https://api.github.com/users/wbh2004-new"
headers = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(url, headers=headers, timeout=10)

print("状态码:", resp.status_code)
print("响应类型:", resp.headers.get("Content-Type"))

data = resp.json()
print("用户名:", data["login"])
print("公开仓库数:", data["public_repos"])
print("创建时间:", data["created_at"])