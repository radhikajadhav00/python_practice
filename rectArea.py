# Program to calculate area and perimeter of a rectangle

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def calculate_perimeter(length, width):
    """Calculate the perimeter of a rectangle"""
    return 2 * (length + width)

def main():
    print("Rectangle Area and Perimeter Calculator")

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    print(f"\nArea of rectangle = {area:.2f} square units")
    print(f"Perimeter of rectangle = {perimeter:.2f} units")

if __name__ == "__main__":
    main()
