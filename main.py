import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

url = 'https://www.fotmob.com/matches/chelsea-vs-benfica/2qwr8a#4685770:tab=stats'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=headers)
print(response.status_code)
