from bs4 import BeautifulSoup
import requests
import csv

url = "https://quotes.toscrape.com/"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
soup = BeautifulSoup(resp.text, "html.parser")
rows = []
quotes = soup.find_all("div", class_="quote")          # 空1：用什么标签 + class_="quote"？
for block in quotes:
    text = block.find("span", class_="text").text.strip()          # 空2：span + class_="text"
    author = block.find("small", class_="author").text.strip()        # 空3：small + class_="author"
    print(f"{text} —— {author}")
    rows.append([text, author])

with open("quotes.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["quote", "author"])   # 表头
    writer.writerows(rows)