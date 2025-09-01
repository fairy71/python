def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operator!")

calculator()








tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Remove Task\n4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")







tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Remove Task\n4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")






import random

while True:
    roll = input("Roll the dice? (y/n): ")
    if roll.lower() == "y":
        print("🎲 You rolled:", random.randint(1, 6))
    else:
        break









import time

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time, end="\r")  # overwrite same line
    time.sleep(1)
