import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def startTimer(pomTime, pomBreak):
    clear()
    pomTimeSeconds = pomTime * 60
    pomBreakSeconds = pomBreak * 60

    workSegmentCounter = 1

    while True:
        # Pomodoro time
        for remaining in range(pomTimeSeconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            percentComplete = (1 - (remaining / pomTimeSeconds)) * 100
            timer = '{:02d}:{:02d}'.format(mins, secs)

            bar_length = 50  # Change this value to adjust the progress bar length
            percentBarCounter = int((percentComplete / 100) * bar_length)
            percentBar = '#' * percentBarCounter + '-' * (bar_length - percentBarCounter)
            
            print(f"\033[KTime left: {timer} | Progress: {percentComplete:.2f}% | [{percentBar}]", end="\r")
            time.sleep(1)
        print(f"\033[KTime left: 00:00 | Progress: 100% | \033[32mWork Segment {workSegmentCounter} Complete\033[m")

        # Break time
        for remaining in range(pomBreakSeconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            percentComplete = (1 - (remaining / pomBreakSeconds)) * 100
            timer = '{:02d}:{:02d}'.format(mins, secs)

            bar_length = 50  # Change this value to adjust the progress bar length
            percentBarCounter = int((percentComplete / 100) * bar_length)
            percentBar = '#' * percentBarCounter + '-' * (bar_length - percentBarCounter)
            
            print(f"\033[KBreak left: {timer} | Progress: {percentComplete:.2f}% | [{percentBar}]", end="\r")
            time.sleep(1)
        print(f"\033[KBreak left: 00:00 | Progress: 100% | \033[32mBreak Segment {workSegmentCounter} Complete\033[m")

        workSegmentCounter +=1
