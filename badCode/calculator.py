#Function that takes number 1 and number 2 and adds them
def addition (x, y):
    return x + y
#Function that takes number 1 and number 2 and subtracts them
def subtraction (x, y):
    return x - y

#Function that takes number 1 and number 2 and multiplies them
def multiplication (x, y):
    return x * y

#Function that takes number 1 and number 2 and divides them
def division (x, y):
    return x / y

## Main function to execute the calculator with a while loop and ask what you need to calculate addition / subtraction / multiplication / division 
def main():
    while True:
        calculate = input("What do you want to calculate: addition / subtraction / multiplication / division ")
        while True:
            try:
                number1 = int(input("What is your first number: "))
                break
            except ValueError:
                print("Please enter a valid number")
        
        while True:
            try:
                number2 = int(input("What is your second number: "))
                break
            except ValueError:
                print("Please enter a valid number")
        
        if(calculate == "addition"):
            print(addition(number1,number2))
            break

        elif(calculate == "subtraction"):
            print(subtraction(number1,number2))
            break

        elif(calculate == "multiplication"):
            print(multiplication(number1,number2))
            break
        
        elif(calculate == "division"):
            print(division(number1,number2))
            break

        else:
            print("calculcation inputed wrong")

if __name__=="__main__":
    main()