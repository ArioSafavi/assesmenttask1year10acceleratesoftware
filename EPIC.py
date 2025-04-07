import requests
def epic():
    api_key = "f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6"  
    base_url = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    params = {
        "api_key": api_key,
        "image":  'epic_RGB_20250404040317.png'
    }
    h = requests.get(base_url, params)
    print(h)

