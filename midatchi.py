from datetime import datetime
import keyboard

running = True
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

blink = False
pet = "(o w o)"
petBlink = "(- w -)"

print("Welcome to midatchi!")

while running:
    if keyboard.is_pressed('shift'):
        userInput = input()
    now = datetime.now()
    timeLastTick = current_time
    current_time = now.strftime("%H:%M:%S")
    if current_time != timeLastTick:
        blink = not blink
        print("Current Time =", current_time)
        if blink:
            print(petBlink)
        else:
            print(pet)

