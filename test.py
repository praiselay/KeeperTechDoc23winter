import sys
import requests
from bs4 import BeautifulSoup
import pandas

def crawl(url):
  resp = requests.get(url)
  html = resp.text
  soup = BeautifulSoup(html, 'html.parser')
  # news = soup.select('.<class tag>')
  print(soup)

crawl("")