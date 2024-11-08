import requests
import csv

# URL for Amsterdam Open Data (hypothetical example, may need adjustment)
url_hotels = 'https://data.amsterdam.nl/api/3/action/datastore_search?resource_id=hotels'
url_hospitals = 'https://data.amsterdam.nl/api/3/action/datastore_search?resource_id=hospitals'

def fetch_data(url):
    response = requests.get(url)
    return response.json()['result']['records']

def save_to_csv(data, file_name):
    keys = data[0].keys()
    with open(file_name, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

hotels_data = fetch_data(url_hotels)
save_to_csv(hotels_data, 'hotels.csv')

hospitals_data = fetch_data(url_hospitals)
save_to_csv(hospitals_data, 'hospitals.csv')

print("CSV files created successfully!")
