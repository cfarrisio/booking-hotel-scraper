import requests
from selectorlib import Extractor

# URL to scrape
url = 'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuALe2aClBsACAdICJDExOTlhMzczLTcwYjYtNDZmYi04ZmQwLWMyZmFmY2Q4YWJiNNgCBeACAQ&aid=304142&ss=Florida&ssne=Florida&ssne_untouched=Florida&lang=en-us&src=index&dest_id=1136&dest_type=region&checkin=2023-07-08&checkout=2023-07-09&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&nflt=class%3D2%3Bclass%3D3'

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('booking.yml')

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract data using the Extractor and the response's text
    data = e.extract(response.text)
    print(data)

    # Check if the data extraction was successful
    if data and 'hotels' in data:
        for hotel in data['hotels']:
            # Process and use the extracted data as needed
            name = hotel.get('name')
            location = hotel.get('location')
            price = hotel.get('price')
            price_for = hotel.get('price_for')
            room_type = hotel.get('room_type')
            beds = hotel.get('beds')
            rating = hotel.get('rating')
            rating_title = hotel.get('rating_title')
            number_of_ratings = hotel.get('number_of_ratings')
            url = hotel.get('url')

            # Print or use the extracted data as per your requirements
            print("Name:", name)
            print("Location:", location)
            print("Price:", price)
            print("Price For:", price_for)
            print("Room Type:", room_type)
            print("Beds:", beds)
            print("Rating:", rating)
            print("Rating Title:", rating_title)
            print("Number of Ratings:", number_of_ratings)
            print("URL:", url)
    else:
        print("Data extraction failed.")
else:
    print("Request failed. Status code:", response.status_code)
