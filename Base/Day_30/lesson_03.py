import random



start = input("Play? yes/no ")
while(start == "yes"):
    number = random.randint(1,10)
    attempts = 0
    while (attempts <3):
        answer = int(input("Enter number "))
        if(answer == number):
            print("Good")
            break
        else:
            if(answer > number):
                print("Too high!!")
            else:
                print("Too low!")
            attempts = attempts + 1
            print("Attempts left: ", 3 - attempts)

    if (attempts == 3):   
        print("Game over!") 
        print("The number was:", number)
        
    again = input("Play again ? yes/no ")
    if ( again == "yes"):
        start = again
    else :
        start = "no"