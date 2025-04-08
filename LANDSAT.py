import requests
def landsat():
    api_key = "f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6"

    lat = float(input("Enter the latitude of the image in North: "))
    lon = float(input("Enter the Longitude of the image in West: "))

    url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&dim=0.5&api_key={api_key}"
    response = requests.get(url)
    h = 1
    with open(str(lat)+str(lon)+ ".png", "wb") as file:
        file.write(response.content)
        h = h + 1