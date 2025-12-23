tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        print("Your Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(i, t)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
