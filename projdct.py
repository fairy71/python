tasks = []  # list to store tasks

def show_menu():
    print("\n To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f" Task added: {task}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet ")
        else:
            print("\n Your Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("⚠ No tasks to remove!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑 Removed task: {removed}")
            else:
                print(" Invalid task number!")

    elif choice == "4":
        print(" Exiting... Goodbye!")
        break

 