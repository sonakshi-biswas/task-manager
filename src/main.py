tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!")
    else:
        print("Invalid number")

def menu():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()