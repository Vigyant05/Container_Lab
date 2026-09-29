def calculator():
    print("===Simple Arithmetic Calculator===")
    print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
    choice=int(input("Enter a choice: "))
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    match choice:
        case 1:
            print(f"Sum: {a+b}")
        case 2:
            print(f"Difference: {a-b}")
        case 3:
            print(f"Product: {a*b}")
        case 4:
            if b==0:
                print("Cannot divide by zero")
            else:
                print(f"Quotient: {a/b:.2f}")
        case _:
            print("Invalid Choice")

calculator()
