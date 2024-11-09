import requests
import simplekml
import os

API_KEY = os.getenv('GOOGLE_API_KEY')
LOCATION = '52.3676,4.9041'  # Coordinates of Amsterdam's city center
RADIUS = 5000  # Search within a 5 km radius
PLACE_TYPES = ['hotel']

kml = simplekml.Kml()

for place_type in PLACE_TYPES:
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LOCATION}&radius={RADIUS}&type={place_type}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    for place in data['results']:
        name = place['name']
        lat = place['geometry']['location']['lat']
        lng = place['geometry']['location']['lng']

        # Add placemark to KML
        kml.newpoint(name=name, coords=[(lng, lat)])

# Save to KMZ file
kml.savekmz('amsterdam_hotels.kmz')

print("KMZ file created successfully!")
