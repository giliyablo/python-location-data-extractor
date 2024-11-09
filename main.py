import requests
import csv
import os

API_KEY = os.getenv('GOOGLE_API_KEY')
LOCATION = '52.3676,4.9041'  # Coordinates of Amsterdam's city center
RADIUS = 5000  # Search within a 5 km radius
PLACE_TYPES = {'hotel': 'hotels.csv', 'hospital': 'hospitals.csv'}

for place_type, file_name in PLACE_TYPES.items():
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LOCATION}&radius={RADIUS}&type={place_type}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    places = []
    for place in data['results']:
        places.append({
            'Name': place['name'],
            'Latitude': place['geometry']['location']['lat'],
            'Longitude': place['geometry']['location']['lng'],
            'Place ID': place['place_id']
        })

    # Write data to CSV file
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Latitude', 'Longitude', 'Place ID'])
        writer.writeheader()
        for place in places:
            writer.writerow(place)

print("CSV files created successfully!")
