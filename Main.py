from APOD import *
from EPIC import *
from LANDSAT import *
from NEOWS import *


def main(): 
    while True:
        choice = input("""What do you want to do?   
                       (Enter 1 to get the astronomy picture of the day (Daily pictures of cool stuff NASA finds)
                        Enter 2 to get EPIC IMAGRY. (Imagery of the Earth)
                        Enter 3 to get lansat Imagary (Satalite imagry of the earth)
                        Enter 4 to get NEOWS information (Near earth objects observation)(This is much more advanced and harder to understand if not familliar)
                       ENTER end to exit the program): """)
        if choice == '1':
            apod()
        elif choice == '2':
            epic()
        elif choice == '3':
            landsat()
        elif choice == '4':
            neows()
        elif choice == 'end':
            break
        else:
            print('Invalid Input Please try again')



if __name__ == "__main__":
    main()