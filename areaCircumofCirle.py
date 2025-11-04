# Program to calculate area and circumference of a circle


import math
def calculate_area(radius):
    """Calculate the area of a circle"""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Calculate the circumference of a circle"""
    return 2 * math.pi * radius

def main():
    print("Circle Area and Circumference Calculator")

    radius = float(input("Enter the radius of the circle: "))

    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    print(f"\nArea of circle = {area:.2f} square units")
    print(f"Circumference of circle = {circumference:.2f} units")

if __name__ == "__main__":
    main()
