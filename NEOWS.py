import requests
import json
api_Key = 'f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6'
def neows():
    try:
        asteroid_id = input('enter one of the following asteroid_ids or enter one you found yourself (2025 DU2, 2022 CE2,2024 YR4 ): ')
        URL_NeoLookup = "https://api.nasa.gov/neo/rest/v1/neo/"+ asteroid_id
        params = {
        'api_key':api_Key,
        }
        response = requests.get(URL_NeoLookup,params=params).json()
        with open(str(asteroid_id)+ 'astroid_data.json','a') as output:
            json.dump(response, output)
    except:
        print('Invalid Asteroid ID')