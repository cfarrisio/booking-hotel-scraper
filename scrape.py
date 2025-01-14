from selectorlib import Extractor
import requests
from time import sleep
import csv
import random

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('booking.yml')

def scrape(url):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://www.booking.com/index.en-gb.html',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s" % url)
    r = requests.get(url, headers=headers)
    # Pass the HTML of the page and create
    data = e.extract(r.text, base_url=url)
    return data

with open("urls.txt", 'r') as urllist, open('data.csv', 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = [
        "name",
        "location",
        "price",
        "price_for",
        "room_type",
        "beds",
        "rating",
        "rating_title",
        "number_of_ratings",
        "url"
    ]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    
    for url in urllist.readlines():
        data = scrape(url.strip())
        if data and 'hotels' in data:
            for hotel in data['hotels']:
                writer.writerow(hotel)
            sleep(random.uniform(3, 5))  # Use random sleep between 3 and 5 seconds
