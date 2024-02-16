import sys
import requests
from bs4 import BeautifulSoup
import pandas

resp = requests.get('<URL>')
html = resp.text
soup = BeautifulSoup(html, 'html.parser')
# news = soup.select('.<class tag>')

print(soup)