retry = 1

while retry == 1:
    print("Welcome to your signified calculator.")

    num1 = int(input("What is your first number: "))
    num2 = int(input("What is your second number: "))

    add = num1+num2
    sub = num1-num2
    mult = num1*num2
    div = num1/num2

    print(f"{num1} + {num2} = {add} \n{num1} - {num2} = {sub} \n{num1} * {num2} = {mult} \n{num1} / {num2} = {div}")

    print("\nHere are the special operators! :")

    exp = num1**num2
    intdiv = num1//num2
    mod = num1%num2

    print(f"\n(Exponent) {num1}^{num2} = {exp} \n(Intiger Division) {num1} // {num2} = {intdiv} \n(Modulus) {num1} % {num2} = {mod}")

    retry = int(input("\nWould you like to try 2 new numbers? \nType '1' to try again! \nType '2' to quit! \n\nInput: "))

    if retry == 2:
        print("\n Thank you for using our trusted calculator!")
        quit()
    else:
        retry = 1
        print("\n")