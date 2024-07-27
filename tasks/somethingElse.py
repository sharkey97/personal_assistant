import time
from utils import clear

def run(username):
    clear()
    print("Executing: Something Else...")
    usersTask = input("Please tell me what you'd like to do, and I'll do my best to execute your command.")

    print(f"You would like me to {usersTask}. Let me see if I can process that for you...")

    taskSegments = usersTask.split(' ')
    print(taskSegments)
    time.sleep(5)
