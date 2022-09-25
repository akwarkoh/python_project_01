#!/usr/bin/env python3
from tkinter import Menu


def main():

    while True:
   #Prompt user to make a selection
        input("===Place your Order=== \n 1. Fried rice with chicken \n 2. Banku and Okro stew \n 3.Peanut Butter soup with Rice balls \n 4. Yam and Spinach Stew \n \n Pick Your Favorite")
    
   #Store user input in a variable
    menu = input("===Place your Order=== \n a. Fried rice with chicken \n b. Banku and Okro stew \n c.Peanut Butter soup with Rice balls \n d. Yam and Spinach Stew \n \n Pick Your Favorite")
   
   #convert user input into an int
    menu = int(input("===Place your Order=== \n a. Fried rice with chicken \n b. Banku and Okro stew \n c.Peanut Butter soup with Rice balls \n d. Yam and Spinach Stew \n \n Pick Your Favorite"))

    if menu == 1:
        print("\n Fried rice with chicken: $15 ")

    #prompt user to confirm selection 
        confirm1 = input("\n Press 1 to confirm: ")
        confirm1 = int(input("\n Press 1 to confirm: "))

        if confirm1 == 1:
            print("\n Thanks for placing your order ")

            #prompt user to choose a different option 
        else:
            int(print("\n Choose another option: "))
             

    elif menu == 2:
        print("\n Banku and Okro stew: $17 ")

        confirm2 = input("\Press 2 to confirm: ")
        confirm2 = int(input("\Press 2 to confirm: "))

        if confirm2 == 2:
            print("\n Thanks for placing your order ")
        else:
            int(input("\n Choose another option: "))

    elif menu == 3:
        print("\n 3.Peanut Butter soup with Rice balls: $14 ") 

        confirm3 = input("\Press 3 to confirm: ")
        confirm3 = int(input("\Press 3 to confirm: ")) 

        if confirm3 == 3:
            print("\n Thanks for placing your order ")
        else:
            int(input("\n Choose another option: "))

    elif menu == 4:
        print("\n Yam and Spinach Stew: $15 ")

        confirm4 = input("\Press 4 to confirm: ")
        confirm4 = int(input("\Press 4 to confirm: "))

        if confirm4 == 4:
            print("\n Thanks for placing your order ")
        else:
            int(input("\n Choose another option: "))

    else:
        print("\n Choose from the provided menu")

main()