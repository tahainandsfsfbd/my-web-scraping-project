from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# Tarayıcıyı başlat
driver = webdriver.Chrome()

# Wikipedia sayfasını aç
url = "https://en.wikipedia.org/wiki/Marshall_Plan"
driver.get(url)

# Sayfanın HTML içeriğini al
html_content = driver.page_source

# BeautifulSoup ile HTML içeriğini analiz et
soup = BeautifulSoup(html_content, "html.parser")

# 1. Başlığı çek (H1 etiketi)
title = soup.find("h1", {"id": "firstHeading"}).text.strip()

# 2. İlk paragrafı çek (Açıklama için)
first_paragraph = soup.find("p").text.strip()

# 3. Diğer paragrafları çek (Tüm <p> etiketleri)
all_paragraphs = soup.find_all("p")
paragraphs = [p.text.strip() for p in all_paragraphs if p.text.strip()]

# Tarayıcıyı kapat
driver.quit()

# 4. Veriyi CSV dosyasına kaydet
with open("marshall_plan.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # CSV başlıkları
    writer.writerow(["Başlık", "Açıklama", "Paragraf"])

    # İlk satıra başlık ve açıklamayı ekle
    writer.writerow([title, first_paragraph, ""])

    # Paragrafları satır satır ekle
    for paragraph in paragraphs:
        writer.writerow(["", "", paragraph])

print("Veriler 'marshall_plan.csv' dosyasına kaydedildi.")