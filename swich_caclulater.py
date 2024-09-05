A=int(input("enter first value"))
B=int(input("enter secoend value"))
operator = input("Enter the operator (+, -, *, /,%): ")
match operator:
    case "+":
        result =A+B
        print(A+B)
    case "-":
        result = A -B
        print(A - B)
    case "*":
        result = A *B
        print(A * B)
    case "/":
        if B!= 0:
            result = A /B
            print(A / B)
        else:
           print("Error: Division by zero!")

    case"%":
        if B!= 0:
            result = A % B
            print(A % B)
        else:
            print("eror")
    case _:
        print("Error: Invalid operator!")

