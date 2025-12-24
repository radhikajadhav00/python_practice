try:
    # Ask the user to enter the marks and convert the input to a float
    marks = float(input("Please enter the marks (0-100): "))

    # Validate that the marks are within a plausible range (0-100)
    if 0 <= marks <= 100:
        # Determine the grade using if-elif-else statements
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        # Display the calculated grade
        print(f"Grade: {grade}")
    else:
        # Handle invalid input outside the 0-100 range
        print("Invalid marks. Please enter a value between 0 and 100.")

except ValueError:
    # Handle cases where the input is not a valid number
    print("Invalid input. Please enter a numeric value.")
    
    
    