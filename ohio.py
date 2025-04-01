import requests

api_key = "f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6"  
base_url = "https://api.nasa.gov/planetary/earth/imagery"
params = {
    "api_key": api_key,
    "lat": 33.8688,
    "lon": 151.2093
    }
ReceivedResponse = False
while not ReceivedResponse:
    try:
        response = requests.get(base_url, params=params)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching APOD: {e}")
        if ("APOD: 429 Client Error: " in str(e)):
            print("Retrying")
        else:
            print('nope')
            break

print('code ended')