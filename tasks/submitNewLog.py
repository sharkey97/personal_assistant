from datetime import datetime
from utils import clear

def run(username):
    clear()
    print("Welcome to the log assistant terminal.")
    logName = input("What is the log subject? ")
    logInput = input(f"Please enter the content of log: {logName} - ")

    personalLogFile = 'logs/personalLogFile.txt'

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(personalLogFile, 'a') as f:
        f.write("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        f.write(f"\nSubmission Time: {current_time}\nUser: {username} \nLog - {logName}\n")
        f.write(logInput)
