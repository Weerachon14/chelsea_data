import requests
# from bs4 import BeautifulSoup
import logging
import os
import json
logging.basicConfig(level=logging.INFO)

def scarping_data():
    url = 'https://www.fotmob.com/matches/chelsea-vs-benfica/2qwr8a#4685770:tab=stats'

    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.fotmob.com/matches/chelsea-vs-benfica/2qwr8a',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvZGF0YS9tYXRjaERldGFpbHM/bWF0Y2hJZD00Njg1NzcwIiwiY29kZSI6MTc1MTcwNjAxNjA0MSwiZm9vIjoicHJvZHVjdGlvbjowMGY3ZjViY2RmZDgzYjZmNmFiMWVkODQxM2YzZTlkMjcxZmE3NDRmLXVuZGVmaW5lZCJ9LCJzaWduYXR1cmUiOiI3NDVGMEQxQTY2RUNFQjgxMjMxREU5RThGQkI2MTc4NyJ9',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
    }

    params = {
        'matchId': '4685770',
    }

    response = requests.get('https://www.fotmob.com/api/data/matchDetails', params=params, headers=headers)

    match_detail = response.json()
    filename = "chelsea_benfica.json"

    save_data(match_detail,filename)

def save_data(data, filename):
    folder_path="/mnt/d/Football_data/chelsea_data/data"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Saved data to {file_path}")

if __name__ == "__main__":
    scarping_data()
