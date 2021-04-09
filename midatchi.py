from datetime import datetime
import sys
import keyboard
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

running = True
blink = False

updateScreen = False

petNameScreen = True
nameNotConfirm = True

statusHunger = "~"
statusFun = "c:"
status3 = "?"

petName = ""
petEyes = "(o w o)"
petBlink = "(- w -)"
pet = petEyes
userInput = ""


def render():
    print(petName + ":\t" + statusHunger + " " + statusFun + " " + status3 + "\n\t"+ userInput +"\n\t" + pet + "\n\t" + current_time)

def petAnimate():
    global pet
    global blink
    if(blink):
        pet = petBlink
    else:
        pet = petEyes

def tick():
    global blink
    blink = not blink
    petAnimate()


titleScreen = True
print("WELCOME TO MIDATCHI!\n~~~~~~~~~~~~~~~~~~~\npress ENTER to play")
while titleScreen:
    if keyboard.is_pressed('enter'):
        titleScreen = False

input.__format__

print("Please enter your pets name:")
while petNameScreen:
    nameNotConfirm = True
    petName = input()
    if petName != "":
        while nameNotConfirm:
            print("Are you sure you want your pet to be named " +
                  petName + "? ('yes'/'no')")
            yesNo = str.lower(input())
            if yesNo == "yes":
                petNameScreen = False
                nameNotConfirm = False
                break
            elif yesNo == "no":
                nameNotConfirm = False

while running:
    now = datetime.now()
    timeLastTick = current_time
    current_time = now.strftime("%H:%M:%S")

    if current_time != timeLastTick:
        
        tick()
        cls()
        render()

    if keyboard.is_pressed('/'):
        cls()
        input.__format__
        print("Input: ")
        userInput = input()

    if keyboard.is_pressed('escape'):
        exit()
