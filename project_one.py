#!/usr/bin/env python3

def main():

    order = 1

    while order == 1:
    
        #Prompt user for an input, store user input in a variable and convert user input into an int
        menu = int(input("===Place your Order=== \n 1. Fried rice with chicken \n 2. Banku and Okro stew \n 3. Peanut Butter soup with Rice balls \n 4. Yam and Spinach Stew \n \n Pick Your Favorite: "))
        


        if menu == 1:
            print("\n Fried rice with chicken: $15")
        
        #prompt user to confirm selection and store in a variable
            confirm1 = int(input("\n Press 1 to confirm: "))

            if confirm1 == 1:
                print("\n Thanks for placing your order")

        #prompt user to choose a different option and covert user input into an int
            else:
                int(print("\n Choose another option: "))
                
        elif menu == 2:
            print("\n Banku and Okro stew: $17 ")
            confirm2 = int(input("\n Press 2 to confirm: "))
        #prompt user to confirm selection and store in a variable
            if confirm2 == 2:
                print("\n Thanks for placing your order")
            else:
                int(input("\n Choose another option: "))


        elif menu == 3:
            print("\n Peanut Butter soup with Rice balls: $14 ") 
            confirm3 = int(input("\n Press 3 to confirm: ")) 

            if confirm3 == 3:
                print("\n Thanks for placing your order")
            else:
                int(input("\n Choose another option: "))


        elif menu == 4:
            print("\n Yam and Spinach Stew: $15")
            confirm4 = int(input("\n Press 4 to confirm: "))

            if confirm4 == 4:
                print("\n Thanks for placing your order!")
            else:
                int(input("\n Choose another option: "))

        else:
            print("\n Choose from the provided menu")

        confirm5 = int(input("\n Press 0 to complete your order and press 1 to continue: "))
        order = confirm5

    print("\n Your order will be ready in 15 minutes")   

main()