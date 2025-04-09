# Importing necessary libraries
import requests                      # For making HTTP requests to the NASA API
import matplotlib.pyplot as plt      # For displaying images
import matplotlib.image as mpimg     # For reading image files
import json                          # For printing JSON data in a readable format

# Define a function to get the Astronomy Picture of the Day (APOD) from NASA's API
def get_apod(date):
    # Ask user for a date or use today's APOD if left blank
    date = input('Enter a date after 1996 in this format: year-month-day (example: 2009-08-24, Press enter for today): ')
    
    # NASA API key and base URL
    api_key = "f9UVGf15EXLQsks5QnAjP7fQZzIlX68vZ2fBfnd6"  
    base_url = "https://api.nasa.gov/planetary/apod"
    
    # Set up parameters for the GET request
    params = {
        "api_key": api_key,
        "date": date
    }

    ReceivedResponse = False  # Flag to keep trying if a 429 error (too many requests) occurs
    
    # Try to fetch the APOD data, retry if necessary
    while not ReceivedResponse:
        try:
            response = requests.get(base_url, params=params)  # Make the API request
            response.raise_for_status()  # Raise an error if status code indicates a problem
            ReceivedResponse = True      # Mark as successful
            return response.json()       # Return the JSON response as a dictionary
        except requests.exceptions.RequestException as e:
            print(f"Error fetching APOD: {e}")
            if "APOD: 429 Client Error:" in str(e):  # If rate-limited, retry
                print("Retrying")
            else:
                return None  # Stop retrying for other types of errors

# Placeholder for date input, not used directly in this version
date_to_fetch = ""

# Main function to fetch, download, and display APOD content
def apod():
    # Call get_apod to fetch data from the API
    apod_data = get_apod(date_to_fetch)

    # Check if valid data was received
    if apod_data:
        # Print all the metadata in a readable JSON format
        print(json.dumps(apod_data, indent=4))

        url = apod_data['url']  # Get the image or video URL
        response = requests.get(url)  # Download the content

        # If the media is an image (not a video), download and display it
        if apod_data["media_type"] != 'video':
            filename = url.split('/')[-1]  # Use the last part of the URL as filename
            with open(filename, 'wb') as file:
                file.write(response.content)  # Save image to local file

            # Load and display the image using matplotlib
            img = mpimg.imread(filename)
            imgplot = plt.imshow(img)
            plt.axis('off')  # Hide axis for better image display
            plt.show()
        else:
            # If it's a video, save the video URL to a text file for later viewing
            with open("VideoURL.txt", "a") as f:
                f.write('     ' + apod_data['title'] + ' ' + url + '\n')
