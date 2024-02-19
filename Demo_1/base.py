retry = "1"

while retry == "1":

    first = input("\n------------------------\nWhat would you like to do today? \n\n1. Calculator \n2. Circle \n\nInput: ")
    if first == "1":
        
        Pick = input("\n------------------------\nWhat would you like to use? \n\n1. Addition \n2. Substraction \n3. Division \n4. Multiplication \n\nInput: ")

        if Pick == "1": ## Addition
            x = int(input("\n------------------------\nWhat is your first number: "))
            y = int(input("What is your second number: "))
            total = x+y
            print(f"\n------------------------\nYour answer is: {total}")

            retry = input("\n------------------------\nWould you like to retry? \n\n(1) Yes \n(2) No \n\nInput: ")

            if retry == "2":
                print("\n\nThank you!")
            elif retry == "1":
                retry = "1"

        elif Pick == "2": ## Substraction
            x = int(input("\n------------------------\nWhat is your first number: "))
            y = int(input("What will you substract it by: "))
            total = x-y
            print(f"\n------------------------\nYour answer is: {total}")

            retry = input("\n------------------------\nWould you like to retry? \n\n(1) Yes \n(2) No \n\nInput: ")

            if retry == "2":
                print("\n\nThank you!")
            elif retry == "1":
                retry = "1"

        elif Pick == "3": ## Multiplication
            x = int(input("\n------------------------\nWhat is your first number: "))
            y = int(input("What is your second number: "))
            total = x*y
            print(f"\n------------------------\nYour answer is: {total}")

            retry = input("\n------------------------\nWould you like to retry? \n\n(1) Yes \n(2) No \n\nInput: ")

            if retry == "2":
                print("\n\nThank you!")
            elif retry == "1":
                retry = "1"

        elif Pick == "4": ## Division
            x = int(input("\n------------------------\nWhat is your first number: "))
            y = int(input("What will you divide it by: "))
            total = x/y
            print(f"\n------------------------\nYour answer is: {total}")
            
            retry = input("\n------------------------\nWould you like to retry? \n\n(1) Yes \n(2) No \n\nInput: ")

            if retry == "2":
                print("\n\nThank you!")
            elif retry == "1":
                retry = "1"

        else:
            print("\nInvalid Input.")
            quit()

    elif first == "2":

        circle = input("\n------------------------\nWhat would you like to do today? \n\n1. Area  \n2. Diameter \n\nInput: ")
        
        if circle == "1":
            radius = float(input("\n------------------------\nWhat is your radius? : "))
            rounding = int(input("How many decimal places? : "))
            from math import pi
            area = pi * radius ** 2
            area = round(area, rounding)

            print(f"\n------------------------\nYour area is {area}")

            retry = input("\n------------------------\nWould you like to retry? \n\n(1) Yes \n(2) No \n\nInput: ")

            if retry == "2":
                print("\n------------------------\nThank you!")
            elif retry == "1":
                retry = "1"
        
        if circle == "2":
            radius = int(input("\n------------------------\nWhat is your radius? : "))
            dia = radius*2

            print(f"\n------------------------\nYour diameter is {dia}")

            retry = input("\n------------------------\nWould you like to retry? \n\n(1) Yes \n(2) No \n\nInput: ")

            if retry == "2":
                print("\n------------------------\nThank you!")
            elif retry == "1":
                retry = "1"
        
        else:
            quit()
    else:
        print("\nInvalid Input.")
        quit()
