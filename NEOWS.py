# Import required libraries
import requests  # To make HTTP requests to the NASA API
import json      # To handle JSON data (read/write)

# NASA API key for authentication
api_Key = 'f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6'

# Function to retrieve NEO (Near Earth Object) data from NASA API
def neows():
    try:
        # Prompt the user to input an asteroid ID
        asteroid_id = input('Enter one of the following asteroid_ids or enter one you found yourself (2025 DU2, 2022 CE2, 2024 YR4): ')

        # Construct the API endpoint URL using the input asteroid ID
        URL_NeoLookup = "https://api.nasa.gov/neo/rest/v1/neo/" + asteroid_id

        # Set up parameters for the GET request, including the API key
        params = {
            'api_key': api_Key,
        }

        # Send a GET request to the API and parse the JSON response
        response = requests.get(URL_NeoLookup, params=params).json()

        # Open (or create) a JSON file named after the asteroid ID to save the response data
        # Mode 'a' is used for appending, but could be 'w' (write) if overwriting is preferred
        with open(str(asteroid_id) + '_astroid_data.json', 'a') as output:
            json.dump(response, output)  # Write the JSON data to the file

    # Handle exceptions, such as invalid asteroid IDs or request failures
    except:
        print('Invalid Asteroid ID')
