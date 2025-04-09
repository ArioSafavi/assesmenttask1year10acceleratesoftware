# Import the requests library to make HTTP requests
import requests

# Define the main function to retrieve a Landsat satellite image from NASA's Earth imagery API
def landsat():
    # NASA API key for authentication
    api_key = "f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6"

    # Try block to handle user input and API request safely
    try:
        # Prompt the user for latitude and longitude coordinates
        lat = float(input("Enter the latitude of the image in North: "))    # e.g., 37.7749
        lon = float(input("Enter the Longitude of the image in West: "))    # e.g., -122.4194

        # Construct the API request URL using the input coordinates
        # 'dim=0.5' specifies the image width and height in degrees
        url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&dim=0.5&api_key={api_key}"

        # Send the GET request to the API
        response = requests.get(url)

        # Set a filename using the lat/lon values to uniquely name the image
        filename = str(lat) + "_" + str(lon) + ".png"

        # Save the image to a file in binary write mode
        with open(filename, "wb") as file:
            file.write(response.content)

        print("Image downloaded successfully.")
        print("If the image does not display correctly, the coordinates may not have satellite data available.")

    # Handle exceptions gracefully (e.g., invalid input or network errors)
    except:
        print("Didn't work: Invalid input or API request failed.")
