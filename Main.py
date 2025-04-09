# Importing all functions from your individual modules
from APOD import *       # Handles Astronomy Picture of the Day
from EPIC import *       # Handles EPIC Earth imagery
from LANDSAT import *    # Handles Landsat satellite imagery
from NEOWS import *      # Handles Near-Earth Object Web Service data

# Main program function
def main(): 
    # Infinite loop to keep the menu running until user exits
    while True:
        # Display the menu and prompt for user choice
        choice = input("""
What do you want to do?   

1 - Get the Astronomy Picture of the Day  
    (Daily pictures of cool stuff NASA finds)

2 - Get EPIC Imagery  
    (Real-time imagery of the Earth taken by NASA's EPIC camera)

3 - Get Landsat Imagery  
    (Satellite imagery of the Earth, useful for geographical and environmental data)

4 - Get NEOWS Information  
    (Data on Near-Earth Objects, such as asteroids — more technical and detailed)

Type 'end' to exit the program.

Enter your choice: """)

        # Check user input and call the appropriate function
        if choice == '1':
            apod()  # Call APOD function
        elif choice == '2':
            epic()  # Call EPIC function
        elif choice == '3':
            landsat()  # Call Landsat function
        elif choice == '4':
            neows()  # Call NEOWS function
        elif choice.lower() == 'end':
            break  # Exit the loop and program
        else:
            # If the input is invalid, prompt again
            print('Invalid input. Please try again.')

# Run the main function if this script is run directly
if __name__ == "__main__":
    main()
