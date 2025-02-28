line ="________________________________________"
def operacao():
    print(line)
    print("Choose an operation:")
    print("'1' for ADDITION")
    print("'2' for SUBTRACTION")
    print("'3' for MULTIPLICATION")
    print("'4' for DIVISION")

    print(line)

    choice=input()
    print("What is the first value?")
    n1=float(input())
    print(line)

    print("What is the second value?")
    n2=float(input())
    print(line)
    if choice=='1':
        result = (n1+n2)
        print(f"{n1} + {n2} =")
        print(result)
        print(f"The result of adding {int(n1)} and {int(n2)} is {int(result)}.")
        input()


    elif choice=='2':
        result = (n1-n2)
        print(f"{n1}-{n2} =")
        print(result)
        print(f"The result of subtracting {int(n2)} from {int(n1)} is {int(result)}.")
        input()

    elif choice=='3':
        result = (n1*n2)
        print(n1, "*", n2, "=")
        print (result)
        print(f"The result of multiplying {int(n1)} by {int(n2)} is {int(result)}.")
        input()

    elif choice=='4':
        if n2 == 0:
            print("Error! Cannot divide by 0.")
        else:
            result = (n1 / n2)
            print(n1, "/", n2, "=")
            print(result)
            print(f"The result of dividing {int(n1)} by {int(n2)} is {int(result)}.")
            input()


operacao()