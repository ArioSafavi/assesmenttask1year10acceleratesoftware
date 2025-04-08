import requests
import json
def epic():
    api_key = "f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6"  
    base_url = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    params = {
        "api_key": api_key,
        "image":  'epic_RGB_20250404040317.png'
    }
    ReceivedResponse = False
    while not ReceivedResponse:
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  
            ReceivedResponse = True
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching APOD: {e}")
            if ("APOD: 429 Client Error: " in str(e)):
                print("Retrying")
            else:
                return 'no'


