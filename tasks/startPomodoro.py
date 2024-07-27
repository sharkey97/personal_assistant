from utils import startTimer

def run(username):
    print("Executing: Pomodoro...")

    defaultTime = 10
    defaultBreak = 5

    isDefault = input("Use default timer settings? (Y/N)")

    if isDefault.lower() == 'y':
        startTimer(defaultTime, defaultBreak)
    else:
        chosenTime = int(input("How many minutes will your work be?"))
        chosenBreak = int(input("How many minutes will your break be?"))

        startTimer(chosenTime, chosenBreak)
