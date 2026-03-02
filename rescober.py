#To-Do List Task
tasks = [
]

def display_menu():
    print("\n==== Your To-Do List ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks left!")
        return
    print("\nYour Tasks:")
    for i, item in enumerate(tasks, 1):
        status = "✓" if item["done"] else "○"
        print(f"{i}. [{status}] {item['task']}")

def mark_done():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                print("Task marked done! ✓")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a number.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed['task']}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a number.")

while True:
    display_menu()
    choice = input("Choose (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Your tasks is done! Goodbye!")
        break
    else:
        print("Choose 1-5 only.")