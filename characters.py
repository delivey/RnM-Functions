import requests
import random

def how_many_characters(): # Checks how many characters there are. As of 2020-07-17, there are 592 character
    generated_character_id = 1
    while True:
        generated_character_id += 1
        url = f"https://rickandmortyapi.com/api/character/{generated_character_id}"
        r = requests.get(url)
        status_code = r.status_code
        if status_code != 200:
            break
    return generated_character_id

def random_character(): # Generates a random character
    generated_character_id = random.randint(1, 592) # Generates a random character id 
    url = f"https://rickandmortyapi.com/api/character/{generated_character_id}"
    r = requests.get(url) # Sends a GET request to the url
    json = r.json() # Parses the GET request's data into JSON
 
    chid = json['id']
    name = json['name']
    status = json['status']
    species = json['species']
    gender = json['gender']
    current_location = json['location']['name']
    pretty_string = f'Id: {chid}, name: {name}, status: {status}, species: {species}, gender: {gender}, current location: {current_location}'
    # return character_id, name, species, gender, current_location # Uncomment if you want the raw data
    return pretty_string # Returns the 'pretty_string' variable

print(random_character())