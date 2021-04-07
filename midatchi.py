from datetime import datetime
import keyboard
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

running = True
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

blink = False
pet = "(o w o)"
petBlink = "(- w -)"

print("Welcome to midatchi!")

while running:
    now = datetime.now()
    timeLastTick = current_time
    current_time = now.strftime("%H:%M:%S")
    if current_time != timeLastTick:
        blink = not blink
        print("Current Time =", current_time)
    if keyboard.is_pressed('shift'):
        print("Current Time =", current_time)
        userInput = input()
    cls()


    if blink:
        print(petBlink)
    else:
        print(pet)

