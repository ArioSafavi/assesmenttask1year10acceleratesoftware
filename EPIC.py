# Import necessary modules
import json                             # For handling JSON data
from urllib.request import urlopen     # For sending HTTP requests using urllib
from datetime import date              # To format and handle dates
import requests                        # For downloading image files

# Main function to fetch and download EPIC (Earth Polychromatic Imaging Camera) images
def epic():
    url_base = "https://epic.gsfc.nasa.gov/"            # Base URL for the EPIC API
    most_recent = url_base + "api/natural"              # Endpoint to get the most recent natural images

    # Function to format a date into a readable string (e.g., 'July 04, 2015')
    def pretty_date(iyear, imonth, iday):
        return date(month=imonth, day=iday, year=iyear).strftime('%B %d, %Y')

    # Function to get the most recent date with available imagery
    def find_most_recent_date():
        print('\nContacting API to find newest image date available...')
        
        data = urlopen(most_recent)                     # Send request to the API
        jdata = json.loads(data.read())                 # Load response as JSON
        for x in jdata:
            most_recent_date = x['identifier']          # The identifier includes the date
        most_recent_date = most_recent_date[:-6]        # Strip last 6 characters to isolate the date (YYYYMMDD)
        return most_recent_date

    # Function to download all images for a specific date and type (e.g., 'natural')
    def download(imagetype):
        try:
            # API endpoint to get metadata for images of the given type and date
            api = url_base + "api/{}/date/{}-{}-{}".format(imagetype, Year, Month, Day)
            # URL to access archived image files
            archive = url_base + "archive/{}/{}/{}/{}/png/".format(imagetype, Year, Month, Day)
        except:
            print("URL construction failed.")
        
        try:
            data = urlopen(api)                         # Request image metadata
            jdata = json.loads(data.read())             # Parse JSON response
            print(imagetype.capitalize() + " images available for {}-{}-{}:".format(Year, Month, Day))
            h = 1                                       # Counter for naming images
            for x in jdata:
                f = (archive + x['image'] + '.png')     # Construct image file URL
                print(f)                                # Print image URL
                img_data = requests.get(f).content      # Download image data
                with open(str(h) + 'n.png', 'wb') as handler:  # Save image locally
                    handler.write(img_data)
                h += 1                                  # Increment image counter
        except:
            print('Problem with connection. Exiting')

    # Start of the main execution

    end_date = find_most_recent_date()                  # Get the most recent image date
    cYear = end_date[:4]                                # Extract year
    cMonth = end_date[4:6]                              # Extract month
    cDay = end_date[6:]                                 # Extract day
    formatted_end_date = '-'.join([cYear, cMonth, cDay])  # Format date for user display

    # Prompt user to enter a date (or press Enter for the most recent one)
    try:
        input_date = input('Enter a date in YYYY-MM-DD format (2015-07-04 thru ' + formatted_end_date + ') (Press Enter for most recent): ')
        if input_date == "":  # If no input, use most recent date
            Year = cYear;  y = int(Year)
            Month = cMonth; m = int(Month)
            Day = cDay; d = int(Day)
            print("No input. Using the most recent date found: {}.".format(pretty_date(y, m, d)))
        else:  # Parse user input into string and integer forms
            Year, Month, Day = map(str, input_date.split('-'))  # Keep string format to preserve leading zeros
            y, m, d = map(int, input_date.split('-'))           # Integer format for date functions
    except:
        print("Invalid Input. Exiting.")

    # Download natural color images for the given date
    download("natural")
