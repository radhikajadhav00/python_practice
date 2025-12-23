# Program to convert kilometers to miles and vice versa

def km_to_miles(kilometers):
    """Convert kilometers to miles"""
    return kilometers * 0.621371

def miles_to_km(miles):
    """Convert miles to kilometers"""
    return miles / 0.621371

def main():
    print("Distance Conversion Program")
    print("1. Convert Kilometers to Miles")
    print("2. Convert Miles to Kilometers")

    # Get user choice
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km_to_miles(km)
        print(f"{km} kilometers is equal to {miles:.2f} miles")

    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles_to_km(miles)
        print(f"{miles} miles is equal to {km:.2f} kilometers")

    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
    
