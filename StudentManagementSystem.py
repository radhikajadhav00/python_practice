students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("Student added!")

def view_students():
    print("\n--- Student List ---")
    for s in students:
        print(s["roll"], "-", s["name"])

while True:
    print("\n1. Add\n2. View\n3. Exit")
    choice = int(input("Choose: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    else:
        break
