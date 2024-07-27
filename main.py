import time
from autoload_tasks import default_tasks, other_tasks
from utils import clear

def startProgram():
    global username
    print('Welcome! Can I first take your name?')
    
    username = input()
    print(f"Hi, {username}")
    print('What shall we do first?')

    taskList = [
        (name, idx + 1, func) 
        for idx, (name, func) in enumerate(default_tasks.items())
    ]

    taskActions = {str(task[1]): task[2] for task in taskList}

    while True:
    # Assuming taskList is a list of tuples with (task_name, task_number)
        for task in taskList:
            print(f"{task[1]}. {task[0]}")

        # Find the highest task number in taskList
        if taskList:
            highest_task_number = max(task[1] for task in taskList)
        else:
            highest_task_number = 0
        
        # Show "Something else" as the next number after the highest task number
        somethingElseTaskNo = highest_task_number + 1
        print(f"{somethingElseTaskNo}. Something Else")

        chosenTask = input("Enter the number of the task you want to choose: ")

        if chosenTask in taskActions:
            print(f"Task {chosenTask} chosen, executing...")
            taskActions[chosenTask](username)  # Pass the username to the task function
        elif chosenTask == str(somethingElseTaskNo):
            print("You chose 'Something else'. Here are more tasks:")
            for idx, (name, func) in enumerate(other_tasks.items(), start=somethingElseTaskNo):
                print(f"{idx}. {name}")
            
            additional_choice = input("Enter the number of the task you want to choose: ")
            additional_choice = int(additional_choice)
            if additional_choice in range(somethingElseTaskNo, somethingElseTaskNo + len(other_tasks)):
                task_name = list(other_tasks.keys())[additional_choice - somethingElseTaskNo]
                print(f"Task {task_name} chosen, executing...")
                other_tasks[task_name](username)
            else:
                print("Invalid choice, returning to the main menu.")
        else:
            print("Invalid choice, please try again.")
        
        continue_choice = input("Do you want to choose another task? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Shutting down program...")
            time.sleep(3)
            break

clear()
if __name__ == "__main__":
    startProgram()
