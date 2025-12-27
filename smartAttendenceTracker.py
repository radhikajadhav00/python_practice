students = {}

while True:
    name = input("Enter student name (or 'exit'): ")
    if name.lower() == "exit":
        break

    status = input("Present / Absent: ").lower()
    students[name] = status

print("\nAttendance Report")
present = 0
for name, status in students.items():
    print(name, ":", status)
    if status == "present":
        present += 1

print("Total Present:", present)
print("Total Absent:", len(students) - present)
