#Importing stuff
import requests
import json

# defining sub functions
def get_apod(date):
    """
    Fetches Astronomy Picture of the Day (APOD) information from NASA API.

    Args:
        date (str): The date in YYYY-MM-DD format.

    Returns:
        dict: A dictionary containing the APOD data, or None if an error occurs.
    """
    date = input('enter a date in this format: year-month-day (example: 2009-08-24)')
    api_key = "f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6"  
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
        "date": date
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
                return None

# defining main functions
date_to_fetch = ""  

def apod():
    x = 0
    while x == 0:
        apod_data = get_apod(date_to_fetch)
        if apod_data:
            print(json.dumps(apod_data, indent=4))
            url = apod_data['url']
            response = requests.get(url)
            filename = url.split('/')[-1] # You can name the file as you want
            with open(filename, 'wb') as file:
                file.write(response.content)
        i = input('do you want to stop?( yes or no )')
        if i == 'yes':
            break
        else:
            print('going again')

# running all of the functions: 
apod()