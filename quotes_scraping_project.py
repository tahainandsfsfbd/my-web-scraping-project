import json
from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Pull all quotes and author names
quotes = soup.find_all("div", class_="quote")
data = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    data.append({"quote": text, "author": author})

# Save data to JSON file 
with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Data saved to JSON file successfully :)")
