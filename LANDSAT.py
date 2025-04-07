import requests
# Import necessary libraries
import earthaccess
import os

def landsat():
    # Authenticate with Earthdata Login
    os.environ['EARTHDATA_LOGIN'] = 'your_earthdata_username'
    os.environ['EARTHDATA_PASSWORD'] = 'your_earthdata_password'

    # Define search parameters
    collection = "LANDSAT_TM_C2"  # Example Landsat Collection
    point = {"type": "Point", "coordinates": [-150, 30]}  # Example coordinates (longitude, latitude)
    date_range = ["2023-01-01", "2023-01-31"]  # Example date range

    # Search for data
    search = earthaccess.search(
        collection=collection,
        intersects=point,
        date=date_range
    )

    # Print the results
    print(search)

    # Download the data
    # (Note: You'll need to specify the desired output path and file format)
    # earthaccess.download(search, output_dir="/path/to/output", format="tif")