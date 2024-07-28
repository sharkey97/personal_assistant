import os

def run(username):
    runtodolist()



# File to store the to-do list
TODO_FILE = "todo_list.txt"

def load_tasks():
    """Load tasks from the file into a list."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save the list of tasks to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(task_number):
    """Delete a task by its number."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed_task}")
    else:
        print(f"Invalid task number: {task_number}")

def runtodolist():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


