def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilomters')


def km_miles():
    km = float(input("enter a distance in kilometers: "))
    miles = km / 1.609
   
    print(f'Distance in miles is: {miles}')

def miles_km():
    miles = float(input("enter a distance in miles: "))
    km = miles * 1.609

    print(f'Distance in kilomters is {km}')


print_menu()

choice = input("which conversion would you like to do? >>> ")

if choice == '1':
    km_miles()
if choice == '2':
    miles_km()