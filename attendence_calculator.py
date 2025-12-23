total_days = int(input("Enter total working days: "))
present_days = int(input("Enter present days: "))

percentage = (present_days / total_days) * 100
print("Attendance percentage:", round(percentage, 2), "%")
