from datetime import datetime
import keyboard
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

running = True
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

blink = False
updateScreen = False

pet = "(o w o)"
petBlink = "(- w -)"

print("Welcome to midatchi!")

while running:
    now = datetime.now()
    timeLastTick = current_time
    current_time = now.strftime("%H:%M:%S")
    if current_time != timeLastTick:
        blink = not blink
        updateScreen = True
        cls()
    if keyboard.is_pressed('shift'):
        print("Current Time =", current_time)
        userInput = input()
    

    if blink:
        if updateScreen:
            updateScreen = False
            print(petBlink + "\n" + current_time)
    else:
        if updateScreen:
            updateScreen = False
            print(pet + "\n" + current_time)

