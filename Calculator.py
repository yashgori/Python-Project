def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y
def Calculator():   
    choice= input ("YNG Calculator \nchoose 1 option \n1. Add \n2. Sub \n3. Multiply \n4. Divide\n")
    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input! Please enter valid numbers.")
        return
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("invalid input")
Calculator()