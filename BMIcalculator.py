def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = calculate_bmi(weight, height)
print("Your BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
