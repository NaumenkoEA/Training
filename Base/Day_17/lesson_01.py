try :
    first_number = int(input("Enter first number :"))
    second_number = int(input("Enter second number :"))
    operation = input("Operation (+,-,*,/) ")
    if(operation == "+"):
        print("Sum: ", first_number + second_number)
    elif(operation == "-"):
        print("Difference: ", first_number - second_number)
    elif(operation == "*"):
            print("Multiplication: ", first_number * second_number)
    elif(operation == "/"):
            if(second_number != 0):
                print("Division: ", first_number / second_number)
            else:
                 print("You cannot divide by zero.")
    else:
         print("Unknown operation.")
    
except ValueError:
    print("Error! Enter a valid numbers.")