try:
    number = int(input("Enter number : "))
except ValueError:
    print("Enter vallid number!")
else:
    print("Number is correct!")
finally:
    print("Program finished.")