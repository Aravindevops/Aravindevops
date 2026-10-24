import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_contributions(username="Aravindevops", output_path="data/contributions.json"):
    url = f"https://github.com/users/{username}/contributions"
    print(f"Fetching {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    days = soup.find_all('td', class_='ContributionCalendar-day')
    data = []
    for day in days:
        date = day.get('data-date')
        level = day.get('data-level')
        if date and level:
            data.append({"date": date, "level": int(level)})
            
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f)
    print(f"Saved {len(data)} days of data to {output_path}")

if __name__ == "__main__":
    fetch_contributions()