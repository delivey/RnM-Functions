import requests
import random

def how_many_locations(): # Checks how many locations there are. As of 2020-07-17, there are 95 locations
    generated_location_id = 1
    while True:
        generated_location_id += 1
        url = f"https://rickandmortyapi.com/api/location/{generated_location_id}"
        r = requests.get(url)
        status_code = r.status_code
        if status_code != 200:
            break
    return generated_location_id

def random_location():
    status_code = 404
    while status_code != 200:
        generated_location_id = random.randint(1, 95)
        url = f"https://rickandmortyapi.com/api/location/{generated_location_id}"
        r = requests.get(url)
        status_code = r.status_code
        json = r.json()
    location_id = json['id']
    name = json['name']
    location_type = json['type']
    dimension = json['dimension']
    return location_id, name, location_type, dimension # Returns the location's id, name, type and dimension.
