import requests
link = 'https://epic.gsfc.nasa.gov/archive/natural/2025/04/06/png/epic_1b_20250406010437.png'
img_data = requests.get(link).content
with open('image.png', 'wb') as handler:
    handler.write(img_data) 