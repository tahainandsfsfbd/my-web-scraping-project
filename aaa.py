import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

# Sayfanın HTML'sini ayrıştır
soup = BeautifulSoup(response.text, "html.parser")

# Üzerinde class="titleline" olan <span>'leri bul
title_spans = soup.find_all("span", class_="titleline")

# Her span içinde <a>'yı bul ve başlığı al
for idx, span in enumerate(title_spans, start=1):
    title = span.find("a").text  # <a> içindeki başlığı al
    print(f"{idx}. {title}")