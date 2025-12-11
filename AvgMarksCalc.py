marks = []
n = int(input("How many subjects? "))

for i in range(n):
    mark = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(mark)

avg = sum(marks) / n
print("Average Marks:", round(avg, 2))
